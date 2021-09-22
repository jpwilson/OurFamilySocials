from django.db import models
from django.contrib.auth import get_user_model


class Location(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True, blank="")

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True, blank="")

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="author"
    )
    description = models.CharField(max_length=400, null=True, blank="")
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    blog = models.TextField(
        null=True, blank=""
    )  # TODO 22Sept  Change this to use tinyMCE or similar......
    # All fields to add in the future
    # TODO 22Sept add a 'last edit date' field
    # TODO 22Sept add a 'django-location-field' field; unrelated, also possibly a 'duration' of album?
    locations = models.ManyToManyField(Location, null=True, blank=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    people = models.ManyToManyField(
        get_user_model(), related_name="people", null=True, blank=True
    )
    # TODO 22Sept - modify people list in form (see queryset in https://medium.com/swlh/django-forms-for-many-to-many-fields-d977dec4b024)
    # TODO 22Sept: Add a 'comments' section/feature
    # TODO 22Sept: Add a 'likes' section/feature

    class Meta:
        ordering = ["title", "description", "pub_date", "author"]

    def __str__(self):
        return self.title


def upload_gallery_image(instance, filename):
    return f"/media/{instance.pet.name}/gallery/{filename}"


class Image(models.Model):
    image = models.ImageField(upload_to=upload_gallery_image)
    caption = models.CharField(max_length=400, null=True, blank="")
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="images")
    locations = models.ManyToManyField(Location, null=True, blank=True)
    # TODO -22Sept21 - add likes and comments...
