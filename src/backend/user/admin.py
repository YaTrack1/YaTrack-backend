from django.contrib import admin

from user.models import User, Employer, Candidate


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = (
        "username",
        "email",
    )
    search_fields = (
        "username",
        "email",
    )
    empty_value_display = "--пусто--"


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
    )
    search_fields = ()
    empty_value_display = "--пусто--"


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "gender",
        "email",
        "telegram",
        "city",
        "birthday",
        "last_visit"

    )
    search_fields = ()
    empty_value_display = "--пусто--"
