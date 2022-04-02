from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Photo(models.Model):
    picture = models.ImageField(null=False, blank=False, verbose_name='Photo', upload_to='uploads')
    caption = models.CharField(null=False, blank=False, verbose_name='Caption', max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
    author = models.ManyToManyField(
        User,
        related_name="photos",
        verbose_name="Author"
    )
    album = models.ForeignKey('webapp.Album', on_delete=models.CASCADE,
                              verbose_name="Album", null=True, blank=True, related_name='photos')
    is_private = models.BooleanField(default=False, verbose_name='Privacy')

    selected = models.ManyToManyField(
        User,
        related_name="selected_photos"
    )
    token = models.CharField(null=True, blank=True, max_length=200)


    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"

    def __str__(self) -> str:
        return f'{self.caption}'


class Album(models.Model):
    name = models.CharField(null=False, blank=False, verbose_name='Name', max_length=100)
    description = models.TextField(null=True, blank=True, verbose_name='Description', max_length=2000)
    author = models.ManyToManyField(
        User,
        related_name="albums",
        verbose_name="Author"
    )
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
    is_private = models.BooleanField(default=False, verbose_name='Privacy')

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"

    def __str__(self) -> str:
        return f'{self.name}'
