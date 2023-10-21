from django.contrib import admin

from tracker.models import (City, Resume, ResumeSkill, Skill, Vacancy,
                            VacancySkill,)
from tracker.models import Candidate


admin.site.register(City)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class VacancySkillInline(admin.TabularInline):
    model = VacancySkill
    extra = 0


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    inlines = (VacancySkillInline,)

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
