from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import EmployerViewset

# ResumeViewset, ComparisonViewset, VacancyViewset, TrackerViewset

app_name = "api"

router = DefaultRouter()

router.register("employer", EmployerViewset, basename="employer")
# router.register("resume", ResumeViewset, basename="resume")
# router.register("comparison", ComparisonViewset, basename="comparison")
# router.register("vacancy", VacancyViewset, basename="vacancy")
# router.register("tracker", TrackerViewset, basename="tracker")

urlpatterns = [
    path("", include(router.urls)),
    path("", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
]
