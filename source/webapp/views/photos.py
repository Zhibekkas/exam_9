from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from webapp.models import Photo
from webapp.forms import PhotoForm

# Create your views here.
class IndexView(LoginRequiredMixin, ListView):
    template_name = 'photos/index_view.html'
    context_object_name = 'photos'
    model = Photo
    ordering = ['-created_at']


class PhotoView(LoginRequiredMixin, DetailView):
    template_name = 'photos/view.html'
    model = Photo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if Photo.objects.filter(is_private=True):
            author = self.object.author.all()
            context['author'] = author
        return context


class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    form_class = PhotoForm
    template_name = "photos/photo_add.html"

    def form_valid(self, form):
        response = super(PhotoCreateView, self).form_valid(form)
        self.object.author.add(self.request.user)
        return response

    def get_success_url(self):
        return reverse('webapp:view', kwargs={'pk': self.object.pk})


class PhotoDeleteView(PermissionRequiredMixin, DeleteView):
    model = Photo
    template_name = "photos/delete.html"
    success_url = reverse_lazy('webapp:index')
    context_object_name = 'photo'
    permission_required = 'webapp.delete_photo'

    def has_permission(self):
        super().has_permission() and self.get_object().author == self.request.user


class PhotoUpdateView(PermissionRequiredMixin, UpdateView):
    model = Photo
    form_class = PhotoForm
    template_name = "photos/edit_photo.html"
    context_object_name = 'photo'
    permission_required = 'webapp.change_photo'

    def get_success_url(self):
        return reverse('webapp:view', kwargs={"pk": self.object.pk})

    def has_permission(self):
        super().has_permission() and self.get_object().author == self.request.user
