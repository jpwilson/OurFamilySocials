from django.http import response
from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from .views import add_album_view, edit_album, delete_album, album_gallery_view
from .models import Album, Image

# TODO once the first set of tests pass, use the test foler and __init__.py
#       as shown here: https://realpython.com/testing-in-django-part-1-best-practices-and-examples/
# TODO use factoryboy
# TODO test the forms and formsets...
class AddAlbumTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        test_user = get_user_model().objects.create_user(  # new
            username="test_user", email="test_user@email.com", password="testpass123"
        )

        Album.objects.create(
            title="My Test Album",
            author=test_user,
            description="Test album description here.",
            blog="This is the contents of the blog field of the test album",
        )

    def test_album_info(self):
        album = Album.objects.get(id=1)
        self.assertEqual("{}".format(album.title), "My Test Album")
