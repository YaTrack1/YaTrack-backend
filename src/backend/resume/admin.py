from django.contrib import admin

from resume.models import Candidate, City, Resume, ResumeSkill


admin.site.register(City)


class ResumeSkillInline(admin.TabularInline):
    model = ResumeSkill
    extra = 0


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('pk', )
    inlines = (ResumeSkillInline,)


class ResumeInline(admin.StackedInline):
    model = Resume
    extra = 0


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "birthday",
        "email",
        "date_create",
    )
    search_fields = (
        "username",
        "email",
    )
    empty_value_display = "--пусто--"
    inlines = (ResumeInline,)
