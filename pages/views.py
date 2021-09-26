# from ofs.albums.models import Album
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.auth import get_user_model
from albums.models import Album


class HomePageView(ListView):
    # model = Album  # is shorthand for: queryset = Publisher.objects.all()
    # user = get_user_model()

    template_name = "home.html"
    context_object_name = "albums"

    def get_queryset(self):
        return Album.objects.filter(author=self.request.user)


class AboutPageView(TemplateView):
    template_name = "about.html"
