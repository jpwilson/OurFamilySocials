from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"
    context_object_name = "jimbo"


class AboutPageView(TemplateView):
    template_name = "about.html"
