from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _


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


# 17
