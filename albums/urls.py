from django.urls import path
from .views import add_album_view


urlpatterns = [
    path("", add_album_view, name="albums"),
]
