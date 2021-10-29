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

    def un_relate(self, removee):
        """
        Dont confuse the two users (FriendList.user and removee's list.user , with the two lists (self , and removee's )
        This takes into account the remover (initiates this) and the removee
        That is, 'remove_relative' has to be called on both parties
        """
        remover_relative_list = self

        remover_relative_list.remove_relative(removee)

        removee_relative_list = FamilyList.objects.get(user=removee)
        removee_relative_list.remove_relative(self.user)
