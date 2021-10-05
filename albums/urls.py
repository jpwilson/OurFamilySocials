from django.urls import path
from .views import add_album_view, album_gallery_view, edit_album, delete_album

app_name = "albums"
urlpatterns = [
    # path("add/", add_album_view, name="add_album"),
    path("add/", add_album_view, name="add_album"),
    path("edit/<int:pk>/", edit_album, name="edit_album"),
    path("delete/<int:pk>/", delete_album, name="delete_album"),
    path("<int:pk>/", album_gallery_view, name="view_album"),
]
