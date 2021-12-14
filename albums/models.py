from django.utils import timezone

from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), null=True, on_delete=models.CASCADE)
    bio = models.CharField(max_length=400, null=True, blank="")

    pub_date = models.DateTimeField("date published", auto_now_add=True)

    @property
    def member_duration(self):
        return timezone.now() - self.pub_date

    """
    MALE = "male"
    FEMALE = "female"
    REFUSE = "refuse"
    GENDER = [
        (MALE, _("Male")),
        (FEMALE, _("Female")),
        (REFUSE, _("Choose not to say")),
    ]
    gender = models.CharField(
        max_length=32,
        choices=GENDER,
        default=REFUSE,
    )
    def save(self, *args, **kwargs):
        created = not self.pk
        super().save(*args, **kwargs)
        if created:
            RelativeList.objects.create(user=self)

    """

    def __str__(self):
        return str(self.user.username)


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance, bio="this is bio of {}".format(instance.username)
        )
        print("We have created a profile via a post save signal")


post_save.connect(create_profile, sender=get_user_model())


def update_profile(sender, instance, created, **kwargs):
    if not created:
        instance.profile.save()
        print("We have now updated a profile via a signal")


post_save.connect(update_profile, sender=get_user_model())


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
    locations = models.ManyToManyField(Location, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    people = models.ManyToManyField(get_user_model(), related_name="people", blank=True)
    # TODO 22Sept - modify people list in form (see queryset in https://medium.com/swlh/django-forms-for-many-to-many-fields-d977dec4b024)
    # TODO 22Sept: Add a 'comments' section/feature
    # TODO 22Sept: Add a 'likes' section/feature

    class Meta:
        ordering = ["title", "description", "pub_date", "author"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("album_detail", kwargs={"pk": str(self.pk)})


# def upload_gallery_image(instance, filename):
#     return f"/media/{instance.album.title}/gallery/{filename}"


class Image(models.Model):
    image = models.ImageField(
        upload_to="pictures/", blank=True
    )  # upload_gallery_image)
    caption = models.CharField(max_length=400, null=True, blank="")
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="images")
    locations = models.ManyToManyField(Location, blank=True)
    pub_date = models.DateTimeField("date published", auto_now_add=True)

    def get_absolute_url(self):
        return reverse("image_detail", kwargs={"pk": str(self.pk)})

    def __str__(self):
        return str(self.caption)

    # TODO -22Sept21 - add likes and comments...
