from django.contrib import admin

from resume.models import City, Resume, ResumeSkill


admin.site.register(City)
admin.site.register(ResumeSkill)


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('pk', )
