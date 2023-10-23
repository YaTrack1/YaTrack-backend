from django.contrib import admin

from user.models import User, Subscription


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
    )
    search_fields = ("username", "email")
    list_filter = ("username", "email")
    empty_value_display = "--пусто--"


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("id", "candidate", "employer")
