from django.db import models
from django.conf import settings
from django.utils import timezone

from django.contrib.auth import get_user_model


# TODO - when we create a new user, we need to create a FamilyList


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
        'Unfried' someone
        Dont confuse the two users (FriendList.user and removee's list.user , with the two lists (self , and removee's )
        This takes into account the remover (initiates this) and the removee
        That is, 'remove_relative' has to be called on both parties
        """
        remover_relative_list = self

        remover_relative_list.remove_relative(removee)

        removee_relative_list = FamilyList.objects.get(user=removee)
        removee_relative_list.remove_relative(self.user)

    def is_relative(self, relative):
        """
        Check if user and relative are linked relatives...
        """
        return relative in self.relatives.all()


class RelativeRequest(models.Model):
    """
    Relative requests - sender & receiver (initiator and receiver)
    """

    # send req, accept req, unsend, unaccept

    sender = models.ForeignKey(
        get_user_model, on_delete=models.CASCADE, related_name="sender"
    )

    receiver = models.ForeignKey(
        get_user_model, on_delete=models.CASCADE, related_name="receiver"
    )

    is_active = models.BooleanField(default=True, null=False, blank=True)

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender.username

    def accept(self):

        receiver_family_list = FamilyList.objects.get(user=self.receiver)

        if receiver_family_list:
            if self.sender not in receiver_family_list:
                receiver_family_list.add_relative(self.sender)

                sender_family_list = FamilyList.objects.get(user=self.sender)
                if sender_family_list:
                    if self.receiver not in sender_family_list:
                        sender_family_list.add_relative(self.receiver)
                        self.is_active = False
                        self.save()

    def decline(self):
        self.is_active = False
        self.save = False

    def cancel(self):
        """
        Functionality same as 'decline', but
        the difference will come with the notification...
        """
        self.is_active = False
        self.save = False
