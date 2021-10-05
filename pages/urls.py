from django.urls import path
from .views import HomePageView, AboutPageView

# app_name = "pages" - namespaces not supported by allauth
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
]
