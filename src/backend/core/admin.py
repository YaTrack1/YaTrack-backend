from django.contrib import admin

from core.models import City, Organization

admin.site.register(Organization)
admin.site.register(City)

# admin.site.register(EmployerVacancies)
# admin.site.register(EmployerOrganization)
