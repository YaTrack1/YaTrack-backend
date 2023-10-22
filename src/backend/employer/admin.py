from django.contrib import admin

from employer.models import (Employer, EmployerVacancies, EmployerOrganization,
                             Organization,)


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
