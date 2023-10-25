from django.contrib import admin

from resume.models import Resume, SkillInResume

# admin.site.register(City)
# admin.site.register(ResumeSkill)


class SkillInResumeInline(admin.StackedInline):
    model = SkillInResume
    extra = 0


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = (SkillInResumeInline,)
