from django.contrib import admin

from tracker.models import (City, EmployerVacancies, EmployerOrganization,
                            Organization, Resume, ResumeSkill, )
from tracker.models import Candidate, Employer
from vacancy.models import Skill, Vacancy, VacancySkill

admin.site.register(City)
admin.site.register(Organization)

class EmployerOrganizationInline(admin.StackedInline):
    model = EmployerOrganization
    extra = 0


class EmployerVacanciesInline(admin.StackedInline):
    model = EmployerVacancies
    extra = 0


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    inlines = (EmployerOrganizationInline, EmployerVacanciesInline,)


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
