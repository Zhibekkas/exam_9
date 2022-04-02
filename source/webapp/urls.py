from django.urls import path
from webapp.views.photos import IndexView, PhotoView, PhotoCreateView, PhotoDeleteView, PhotoUpdateView
app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('photo/<int:pk>/', PhotoView.as_view(), name="view"),
    path('photo/add/', PhotoCreateView.as_view(), name="photo_add"),
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name="delete_photo"),
    path('photo/<int:pk>/edit/', PhotoUpdateView.as_view(), name="edit_photo")

]