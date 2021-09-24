from django.urls import path
from .views import add_album_view, album_gallery_view


urlpatterns = [
    path("add/", add_album_view, name="albums"),
    path("<int:pk>/", album_gallery_view, name="album"),
]
