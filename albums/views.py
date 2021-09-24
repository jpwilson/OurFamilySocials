from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.forms import modelformset_factory
from .models import Image, Album
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
        album_form = AlbumForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES)

        if album_form.is_valid() and formset.is_valid():
            album_obj = album_form.save(commit=False)
            album_obj.author = request.user
            album_obj.save()

            for form in formset.cleaned_data:
                if form:
                    image = form["image"]
                    Image.objects.create(
                        image=image, album=album_obj, caption=form["caption"]
                    )
            return HttpResponseRedirect("")
        else:
            print(album_form.errors, formset.errors)


def album_gallery_view(request, pk):
    album = Album.objects.get(id=pk)
    return render(request, "albums/gallery.html", {"album": album})
