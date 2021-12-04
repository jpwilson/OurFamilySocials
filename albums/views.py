from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView
from django.forms import modelformset_factory, inlineformset_factory
from django.urls import reverse
from .models import Image, Album
from .forms import ImageForm, AlbumForm


class AlbumListView(LoginRequiredMixin, ListView):
    template_name = "albums/album_list.html"
    context_object_name = "albums"

    def get_queryset(self):
        return Album.objects.filter(author=self.request.user)


# TODO NNB! test these views!
# TODO change name from add_album_view to: add_album
# TODO the 'cancel' button on edit page should go back to album_view, not homepage (list of albums)
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
            return HttpResponseRedirect(
                reverse("albums:view_album", args=(album_obj.id,))
            )
        else:
            # print("Out errors are: ", album_form.errors, formset.errors)
            return render(
                request,
                "albums/index.html",
                {
                    "album_form": album_form,
                    "formset": formset,
                    "album_errors": album_form.errors,
                    "form_errors": formset.errors,
                },
            )


def edit_album(request, pk):
    ImageFormSet = inlineformset_factory(Album, Image, form=ImageForm, extra=2)
    album = Album.objects.get(id=pk)

    if request.method == "GET":
        album_form = AlbumForm(instance=album)
        formset = ImageFormSet(queryset=Image.objects.none())
        return render(
            request, "albums/index.html", {"album_form": album_form, "formset": formset}
        )
    elif request.method == "POST":
        album_form = AlbumForm(request.POST, instance=album)
        formset = ImageFormSet(request.POST, request.FILES)

        if album_form.is_valid() and formset.is_valid():
            print("Things are VALIDIO!!!")
            album_obj = album_form.save(commit=False)
            album_obj.author = request.user
            album_obj.save()

            for form in formset.cleaned_data:
                if form:
                    image = form["image"]
                    Image.objects.create(
                        image=image, album=album_obj, caption=form["caption"]
                    )
            return HttpResponseRedirect(
                reverse("albums:view_album", args=(album_obj.id,))
            )
        else:
            print(album_form.errors, formset.errors)


def delete_album(request, pk):
    album = Album.objects.get(id=pk)
    if request.method == "POST":
        album.delete()
        return HttpResponseRedirect(reverse("home"))

    return render(request, "albums/delete.html", {"album": album})


def album_gallery_view(request, pk):
    album = Album.objects.get(id=pk)
    return render(request, "albums/gallery.html", {"album": album})
