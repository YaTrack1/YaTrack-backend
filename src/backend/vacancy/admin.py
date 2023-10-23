from django.contrib import admin

from vacancy.models import Skill, Vacancy, JobSkill, JobTitle


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name",)


class JobSkillInline(admin.TabularInline):
    model = JobSkill
    extra = 0


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(JobTitle)
class JobTitleAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = (JobSkillInline,)
