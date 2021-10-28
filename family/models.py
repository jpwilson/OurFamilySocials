from django.db import models
from django.conf import settings
from django.utils import timezone

from django.contrib.auth import get_user_model


class FamilyList(models.Model):

    user = models.OneToOneField(
        get_user_model, on_delete=models.CASCADE, related_name="user"
    )
    relatives = models.ManyToManyField(
        get_user_model, blank=True, related_name="relatives"
    )

    def __str__(self) -> str:
        return self.user.username

    def add_relative(self, account):
        """
        Add a new relative
        """
        if not account in self.relatives.all():
            self.relatives.add(account)

    def remove_relative(self, account):
        """
        Remove a relative
        """
        if account in self.relatives.all():
            self.relatives.remove(account)
