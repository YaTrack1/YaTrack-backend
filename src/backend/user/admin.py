from django.contrib import admin

from user.models import User


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
