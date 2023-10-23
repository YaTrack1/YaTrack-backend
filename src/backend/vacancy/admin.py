from django.contrib import admin

from vacancy.models import (EmployerVacancies, EmployerOrganization,
                            Organization, Skill, Vacancy, JobSkill, JobTitle)

admin.site.register(EmployerVacancies)
admin.site.register(Organization)
admin.site.register(EmployerOrganization)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class JobSkillInline(admin.TabularInline):
    model = JobSkill
    extra = 0


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(JobTitle)
class JobTitleAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    inlines = (JobSkillInline,)
