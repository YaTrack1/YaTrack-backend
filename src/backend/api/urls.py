from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from api.views import EmployerViewset

# ResumeViewset, ComparisonViewset, VacancyViewset,
# TrackerViewset, FavoriteViewset, InvitationViewset,

app_name = "api"

router = DefaultRouter()

router.register("employer", EmployerViewset, basename="employer")

# router.register("vacancy", VacancyViewset, basename="vacancy")
# router.register("vacancy/create/step-1", VacancyViewset, basename="step-1")
# router.register("vacancy/create/step-2", VacancyViewset, basename="step-2")

# router.register("resume", ResumeViewset, basename="resume")

# router.register("tracker/comparison", ComparisonViewset, basename="tracker")
# router.register("tracker/favorite", FavoriteViewset, basename="favorite")
# router.register(
# "tracker/invitation", InvitationViewset, basename="invitation")

urlpatterns = [
    re_path(r"^", include(router.urls)),
    path("auth/", include("djoser.urls")),
    re_path(r"auth/", include("djoser.urls.authtoken")),
    re_path(r"auth/", include("djoser.urls.jwt")),
]
