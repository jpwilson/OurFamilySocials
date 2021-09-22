from django.shortcuts import render
from django.forms import modelformset_factory
from .models import Image
from .forms import ImageForm, AlbumForm


def add_album_view(request):
    ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=10)

    if request.method == "GET":
        album_form = AlbumForm()
        formset = ImageFormSet(queryset=Image.objects.none())
        return render(
            request, "albums/index.html", {"album_form": album_form, "formset": formset}
        )
    elif request.method == "POST":
        pass
