from django.contrib import admin

from resume.models import Resume, SkillInResume, Experience, Education

# admin.site.register(City)
# admin.site.register(ResumeSkill)


class ExperienceInline(admin.StackedInline):
    model = Experience
    extra = 0


class EducationInline(admin.StackedInline):
    model = Education
    extra = 0


class SkillInResumeInline(admin.StackedInline):
    model = SkillInResume
    extra = 0


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    # list_display = ("title",)
    inlines = (
        SkillInResumeInline,
        ExperienceInline,
        EducationInline,
    )
