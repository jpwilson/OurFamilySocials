from django.urls import path
from .views import HomePageView, AboutPageView, ProfileView

# app_name = "pages" - namespaces not supported by allauth
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("profile/<int:pk>/", ProfileView.as_view(), name="profile"),
]
