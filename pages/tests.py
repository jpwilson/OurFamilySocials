from django.http import response
from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from .views import AboutPageView, HomePageView

# TODO Swith to j setUpTestData class for full test setup at class level (for effic) p83 dfp
class LoggedInHomePageTests(TestCase):
    def setUp(self):
        test_user = get_user_model().objects.create_user(  # new
            username="test_user", email="test_user@email.com", password="testpass123"
        )
        test_user.save()
        # self.client.login(username=test_user.username, password=test_user.password)
        login = self.client.login(username="test_user", password="testpass123")
        url = reverse("home")
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template_used(self):
        self.assertTemplateUsed(self.response, "home.html")

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, "Homepage")

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_homepage_url_resolves_homepageview(self):  # new
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class LoggedOutHomePageTests(TestCase):
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 302)


class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("about")
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, "about.html")

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, "About Our Family Socials")

    def test_aboutpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve("/about/")
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)
