from django.urls import include, re_path
from rest_framework.routers import DefaultRouter

from api.views import (
    EmployerViewset,
    TrackerViewset,
    ComparisonViewset,
    # FavoriteViewset,
    # InvitationViewset,
    VacancyViewset,
    ResumeViewset,
)

app_name = "api"

router = DefaultRouter()

router.register("employer", EmployerViewset, basename="employer")
router.register("employer/vacancy", VacancyViewset, basename="vacancy")
router.register(
    "employer/vacancy/create/step-1", VacancyViewset, basename="step-1"
)
router.register(
    "employer/vacancy/create/step-2", VacancyViewset, basename="step-2"
)

router.register("resume", ResumeViewset, basename="resume")

router.register("tracker", TrackerViewset, basename="tracker")
router.register(
    "tracker",
    ComparisonViewset,
    basename="comparison",
)
# router.register(
#     r"tracker/(?P<vacancy_id>\d+)/comparison",
#     ComparisonViewset,
#     basename="comparison",
# )
# router.register(
#     r"tracker/(?P<vacancy_id>\d+)/favorite",
#     FavoriteViewset,
#     basename="favorite",
# )
# router.register(
#     r"tracker/(?P<vacancy_id>\d+)/invitation",
#     InvitationViewset,
#     basename="invitation",
# )

urlpatterns = [
    re_path(r"^", include(router.urls)),
]
