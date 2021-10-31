from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.db import models
from .models import RelativeList, RelativeRequest


class RelativeListAdmin(admin.ModelAdmin):
    list_filter = ["user"]
    list_display = ["user"]
    search_fields = ["user"]
    readonly_fields = ["user"]

    class Meta:
        model = RelativeList


admin.site.register(RelativeList, RelativeListAdmin)


class RelativeRequestAdmin(admin.ModelAdmin):

    list_filter = ["sender", "receiver"]
    list_display = ["sender", "receiver"]
    search_fields = [
        "sender__username",
        "sender__email" "receiver__username",
        "receiver__email",
    ]

    class Meta:
        model = RelativeRequest


admin.site.register(RelativeRequest, RelativeRequestAdmin)
