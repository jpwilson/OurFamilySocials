from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _
from family.models import RelativeList


class CustomUser(AbstractUser):
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
