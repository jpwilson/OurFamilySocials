"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django Admin
    path("admin/", admin.site.urls),
    # User mgmt
    path("accounts/", include("allauth.urls")),
    # Local apps
    # no longer necessary -> using allauth  path("accounts/", include("accounts.urls")),
    path("", include("pages.urls")),
    path("albums/", include("albums.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# TODO Delete accounts/urls.py and accounts/view.py - no longer needed as using
# allauth pkg (pg 109 of dfp)
# We have also deleted registration folder in templates dir (also see p109 of dfp)
