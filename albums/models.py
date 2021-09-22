from django.db import models
from django.contrib.auth import get_user_model


class Location(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="author"
    )
    description = models.CharField(max_length=400)
    pub_date = models.DateTimeField("date published")
    blog = (
        models.TextField()
    )  # TODO 22Sept  Change this to use tinyMCE or similar......
    # All fields to add in the future
    # TODO 22Sept add a 'last edit date' field
    # TODO 22Sept add a 'django-location-field' field; unrelated, also possibly a 'duration' of album?
    locations = models.ManyToManyField(Location)
    tags = models.ManyToManyField(Tag)
    people = models.ManyToManyField(get_user_model(), related_name="people")
    # TODO 22Sept - modify people list in form (see queryset in https://medium.com/swlh/django-forms-for-many-to-many-fields-d977dec4b024)
    # TODO 22Sept: Add a 'comments' section/feature
    # TODO 22Sept: Add a 'likes' section/feature

    class Meta:
        ordering = ["title", "description", "pub_date", "author"]

    def __str__(self):
        return self.title
