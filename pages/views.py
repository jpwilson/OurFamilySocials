from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth import get_user_model
from albums.models import Album


class HomePageView(LoginRequiredMixin, ListView):
    # model = Album  # is shorthand for: queryset = Publisher.objects.all()
    # user = get_user_model()

    template_name = "home.html"
    context_object_name = "albums"

    def get_queryset(self):
        return Album.objects.filter(author=self.request.user)


class AboutPageView(TemplateView):
    template_name = "about.html"


class ProfileView(DetailView):
    model = get_user_model()
    template_name = "account/profile.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["your_recent_albums"] = Album.objects.filter(
            author=self.request.user
        ).order_by("-pub_date")[:3]
        context["all_albums"] = Album.objects.all()

        return context
