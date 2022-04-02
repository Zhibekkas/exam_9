from django.urls import path
from webapp.views.photos import IndexView, PhotoView, PhotoCreateView, TokenLinkView, PhotoDeleteView, PhotoTokenView,PhotoUpdateView, SelectedPhotoView, PhotoUnselectView
from webapp.views.albums import AlbumCreateView, AlbumDeleteView, AlbumDetailView, AlbumUpdateView
app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('photo/<int:pk>/', PhotoView.as_view(), name="view"),
    path('photo/add/', PhotoCreateView.as_view(), name="photo_add"),
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name="delete_photo"),
    path('photo/<int:pk>/edit/', PhotoUpdateView.as_view(), name="edit_photo"),
    path('album/add/', AlbumCreateView.as_view(), name='album_add'),
    path('album/<int:pk>/update/', AlbumUpdateView.as_view(), name='album_update'),
    path('album/<int:pk>/delete/', AlbumDeleteView.as_view(), name='album_delete'),
    path('album/<int:pk>/', AlbumDetailView.as_view(), name="album_view"),
    path('photo/<int:pk>/select/', SelectedPhotoView.as_view(), name="select"),
    path('photo/<int:pk>/unselect/', PhotoUnselectView.as_view(), name="unselect"),
    path('photo/<int:pk>/token/', PhotoTokenView.as_view(), name='photo_token'),
    path('photo/<uuid:token>/token/', TokenLinkView.as_view(), name='token_link')

]