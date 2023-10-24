from django.shortcuts import get_object_or_404
from djoser.views import UserViewSet as DjoserUserViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

# response, status,
# from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

# , IsAuthenticated

from user.models import User
from core.models import Organization, City, Skill
from tracker.models import Tracker, Comparison, Favorite, Invitation
from resume.models import Resume, SkillInResume
from vacancy.models import Vacancy, SkillInVacancy
from api.serializers import (
    EmployerSerializer,
    CandidateSerializer,
    OrganizationSerializer,
    CitySerializer,
    SkillSerializer,
    TrackerSerializer,
    ComparisonSerializer,
    # FavoriteSerializer,
    InvitationSerializer,
    ResumeSerializer,
    ResumeReadListSerializer,
    ResumeCreateSerializer,
    SkillInResumeSerializer,
    VacancySerializer,
    VacancyReadListSerializer,
    VacancyCreateSerializer,
    SkillInVacancySerializer,
)

# from api.permissions import *
# from api.filters import *
from api.pagination import LimitPageNumberPagination


class EmployerViewset(DjoserUserViewSet):
    """DjoserViewSet нанимателя."""

    queryset = User.objects.all().order_by("id")
    serializer_class = EmployerSerializer
    pagination_class = LimitPageNumberPagination


class CandidateViewset(viewsets.ModelViewSet):
    """DjoserViewSet кандидата."""

    queryset = User.objects.all().order_by("id")
    serializer_class = CandidateSerializer
    # permission_classes =
    pagination_class = LimitPageNumberPagination
    # filterset_class =


class OrganizationViewset(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    # permission_classes =
    pagination_class = LimitPageNumberPagination
    # filterset_class =


class CityViewset(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    # permission_classes =
    pagination_class = LimitPageNumberPagination
    # filterset_class =


class SkillViewset(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = (AllowAny,)
    pagination_class = LimitPageNumberPagination
    # filterset_class =


class TrackerViewset(viewsets.ModelViewSet):
    queryset = Tracker.objects.all()
    serializer_class = TrackerSerializer
    # permission_classes =
    pagination_class = LimitPageNumberPagination
    # filterset_class =


class ComparisonViewset(viewsets.ModelViewSet):
    queryset = Comparison.objects.all()
    serializer_class = ComparisonSerializer
    # permission_classes =
    pagination_class = LimitPageNumberPagination
    # filterset_class =


# class FavoriteViewset(viewsets.ModelViewSet):
#     queryset = Favorite.objects.all()
#     serializer_class = FavoriteSerializer
#     # permission_classes =
#     pagination_class = LimitPageNumberPagination
#     # filterset_class =


class FavoriteViewset(viewsets.ReadOnlyModelViewSet):
    """Viewset-класс для получение избранных."""

    queryset = Favorite.objects.all()
    serializer_class = ResumeSerializer
    # permission_classes = должен быть только автор
    filter_backends = (DjangoFilterBackend,)
    pagination_class = LimitPageNumberPagination
    # filterset_fields = ('gender',)  # gender для проверки filter

    def get_queryset(self):
        # if self.request.user.is_anonymous:
        #     # !!!!!!!!!!!!!!!!!! Возможно ли? какое действие? !!!!!!!!!!!!!
        #     return
        vacancy = get_object_or_404(Vacancy, id=self.kwargs.get("vacancy_id"))
        # if (self.request.user.id == vacancy.author):  # permission
        #     return
        ids = Favorite.objects.filter(vacancy_id=vacancy.id).values_list(
            "resume_id", flat=True
        )
        resumes = Resume.objects.filter(id__in=ids)
        return resumes


class InvitationViewset(viewsets.ModelViewSet):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer
    # permission_classes =
    pagination_class = LimitPageNumberPagination
    # filterset_class =


class ResumeViewset(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    # permission_classes =
    pagination_class = LimitPageNumberPagination
    # filterset_class =

    def get_serializer_class(self):
        if self.request.method in ("POST", "PUT", "PATCH"):
            return ResumeCreateSerializer
        return ResumeReadListSerializer


class SkillInResumeViewset(viewsets.ModelViewSet):
    queryset = SkillInResume.objects.all()
    serializer_class = SkillInResumeSerializer
    # permission_classes =
    pagination_class = LimitPageNumberPagination
    # filterset_class =


class VacancyViewset(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    # permission_classes =
    pagination_class = LimitPageNumberPagination
    # filterset_class =

    def get_serializer_class(self):
        if self.request.method in ("POST", "PUT", "PATCH"):
            return VacancyCreateSerializer
        return VacancyReadListSerializer


class SkillInVacancyViewset(viewsets.ModelViewSet):
    queryset = SkillInVacancy.objects.all()
    serializer_class = SkillInVacancySerializer
    # permission_classes =
    pagination_class = LimitPageNumberPagination
    # filterset_class =
