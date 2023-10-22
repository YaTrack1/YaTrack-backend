from django.contrib import admin

from employer.models import (EmployerVacancies, EmployerOrganization,
                             Organization,)


admin.site.register(EmployerVacancies)
admin.site.register(Organization)
admin.site.register(EmployerOrganization)
