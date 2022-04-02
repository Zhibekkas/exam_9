from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Photo(models.Model):
    picture = models.ImageField(null=False, blank=False, verbose_name='Photo', upload_to='uploads')
    caption = models.CharField(null=False, blank=False, verbose_name='Caption', max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
    author = models.ForeignKey(
        User,
        related_name="photos",
        on_delete=models.CASCADE,
        default=1,
        verbose_name="Author",
        null=False,
        blank=False
    )
    album = models.ForeignKey('webapp.Album', on_delete=models.CASCADE,
                              verbose_name="Album", null=True, blank=True)
    is_private = models.BooleanField(default=False, verbose_name='Privacy')

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"

    def __str__(self) -> str:
        return f"info: {self.caption}. {self.author.username}"


class Album(models.Model):
    name = models.CharField(null=False, blank=False, verbose_name='Name', max_length=100)
    description = models.TextField(null=True, blank=True, verbose_name='Description', max_length=2000)
    author = models.ForeignKey(
        User,
        related_name="albums",
        on_delete=models.CASCADE,
        default=1,
        verbose_name="Author",
        null=False,
        blank=False
    )
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
    is_private = models.BooleanField(default=False, verbose_name='Privacy')

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"

    def __str__(self) -> str:
        return f"info: {self.name}"
