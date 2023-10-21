from django.contrib import admin

from tracker.models import Resume, Skill, Vacancy, VacancySkill
from user.models import Candidate


# @admin.register(Skill)
# class SkillAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
# 
# 
# @admin.register(Vacancy)
# class VacancyAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')



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


class ResumeInline(admin.StackedInline):
    model = Resume
    extra = 0


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "last_visit",
    )
    inlines = (ResumeInline,)
