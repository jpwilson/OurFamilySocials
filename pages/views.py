from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.auth import get_user_model
from albums.models import Album


# TODO add a homepage for 'not logged in' users...
class HomePageView(LoginRequiredMixin, ListView):
    # model = Album  # is shorthand for: queryset = Publisher.objects.all()
    # user = get_user_model()

    template_name = "home.html"
    context_object_name = "albums"

    def get_queryset(self):
        return Album.objects.filter(author=self.request.user)


class AboutPageView(TemplateView):
    template_name = "about.html"
