from django.contrib import admin

from vacancy.models import Skill, Vacancy, VacancySkill


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
