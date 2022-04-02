from django.contrib import admin
from webapp.models import Photo, Album


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'picture', 'caption', 'created_at', 'album', 'is_private']
    list_filter = ['author']
    search_fields = ['caption', 'author']
    fields = ['picture', 'caption', 'created_at', 'author', 'album', 'is_private']
    readonly_fields = ['created_at']


class AlbumAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'creation_date', 'is_private']
    list_filter = ['name']
    search_fields = ['name']
    fields = ['name', 'description', 'author', 'creation_date', 'is_private']
    readonly_fields = ['creation_date']


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Album, AlbumAdmin)
