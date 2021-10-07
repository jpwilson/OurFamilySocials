from django.http import response
from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from django.core.files.uploadedfile import SimpleUploadedFile
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

        Image.objects.create(
            image=SimpleUploadedFile(
                "file.jpg", b"file_content", content_type="image/jpeg"
            ),
            caption="Test Image Caption",
            album=Album.objects.get(id=1),
        )

    def setUp(self):
        self.album = Album.objects.get(id=1)
        self.image = Image.objects.get(id=1)
        url = reverse("albums:view_album", kwargs={"pk": str(self.album.pk)})
        self.response = self.client.get(url)

    def test_album_info(self):
        # album = Album.objects.get(id=1)
        self.assertEqual("{}".format(self.album.title), "My Test Album")

    def test_image_info(self):
        # image = Image.objects.get(id=1)
        self.assertEqual("{}".format(self.image.caption), "Test Image Caption")

    def test_album_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_album_page_template_used(self):
        self.assertTemplateUsed(self.response, "albums/gallery.html")

    def test_album_page_contains_correct_html(self):
        self.assertContains(self.response, "Album")

    def test_album_page_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_album_page_url_resolves_homepageview(self):
        view = resolve("/albums/{}/".format(str(self.album.pk)))
        self.assertEqual(view.func.__name__, album_gallery_view.__name__)
