from django.contrib import admin

from tracker.models import Tracker, Comparison, Favorite, Invitation


@admin.register(Tracker)
class TrackerAdmin(admin.ModelAdmin):
    list_display = ("resume",)
    search_fields = ("resume",)
    list_filter = ("resume",)
    empty_value_display = "--пусто--"


@admin.register(Comparison)
class ComparisonAdmin(admin.ModelAdmin):
    list_display = (
        "resume",
        "vacancy",
    )
    search_fields = (
        "resume",
        "vacancy",
    )
    list_filter = (
        "resume",
        "vacancy",
    )
    empty_value_display = "--пусто--"


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = (
        "resume",
        "vacancy",
    )
    search_fields = (
        "resume",
        "vacancy",
    )
    list_filter = (
        "resume",
        "vacancy",
    )
    empty_value_display = "--пусто--"


@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    list_display = (
        "resume",
        "vacancy",
    )
    search_fields = (
        "resume",
        "vacancy",
    )
    list_filter = (
        "resume",
        "vacancy",
    )
    empty_value_display = "--пусто--"
