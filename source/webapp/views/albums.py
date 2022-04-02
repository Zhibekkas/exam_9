from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from webapp.models import Photo, Album
from webapp.forms import AlbumForm
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse


class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    form_class = AlbumForm
    template_name = "albums/create.html"

    def form_valid(self, form):
        response = super(AlbumCreateView, self).form_valid(form)
        self.object.author.add(self.request.user)
        return response

    def get_success_url(self):
        return reverse('webapp:album_view', kwargs={'pk': self.object.pk})


class AlbumDeleteView(PermissionRequiredMixin, DeleteView):
    model = Album
    permission_required = 'webapp.delete_album'

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("webapp:index")

    def has_permission(self):
        super().has_permission() and self.get_object().author == self.request.user


class AlbumDetailView(LoginRequiredMixin, DetailView):
    template_name = 'albums/view.html'
    model = Album
    context_object_name = 'album'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photos = self.object.photos.order_by("-created_at")
        author = self.object.author.all()
        context['photos'] = photos
        context['author'] = author
        return context


class AlbumUpdateView(PermissionRequiredMixin, UpdateView):
    model = Album
    template_name = 'albums/update.html'
    form_class = AlbumForm
    permission_required = 'webapp.change_album'

    def get_success_url(self):
        return reverse("webapp:album_view", kwargs={"pk": self.object.pk})

    def has_permission(self):
        super().has_permission() and self.get_object().author == self.request.user
