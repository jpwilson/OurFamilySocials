from django import forms
from .models import Album, Image


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ("title", "description", "blog", "locations", "people", "tags")


class ImageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        self.fields["caption"].required = True

    class Meta:
        model = Image
        fields = ("image", "caption")  # TODO - add this to 'edit' later, "locations")
