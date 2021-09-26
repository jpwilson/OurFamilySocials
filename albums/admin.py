from django.contrib import admin
from .models import Album, Image


class AlbumAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "description")
    fields = ["title", "author", "description"]


admin.site.register(Album, AlbumAdmin)
admin.site.register(Image)
