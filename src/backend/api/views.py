from django.shortcuts import get_object_or_404
from djoser.views import UserViewSet as DjoserUserViewSet

# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, response, status, serializers
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated

from user.models import User
from core.models import Skill

# , Organization, City
from tracker.models import Tracker, Comparison, Favorite, Invitation
from resume.models import Resume

# , SkillInResume
from vacancy.models import Vacancy

# , SkillInVacancy
from api.serializers import (
    EmployerSerializer,
    CandidateSerializer,
    # OrganizationSerializer,
    # CitySerializer,
    SkillSerializer,
    TrackerSerializer,
    ComparisonSerializer,
    FavoriteSerializer,
    InvitationSerializer,
    ResumeSerializer,
    ResumeInTrackerSerializer,
    ResumeCreateSerializer,
    # SkillInResumeSerializer,
    VacancySerializer,
    VacancyReadListSerializer,
    VacancyCreateSerializer,
    # SkillInVacancySerializer,
)

# from api.permissions import IsAuthor,
# from api.filters import SkillFilter, ComparisonFilter
from api.pagination import LimitPageNumberPagination


class EmployerViewset(DjoserUserViewSet):
    """DjoserViewSet нанимателя."""

    queryset = User.objects.all().order_by("id")
    serializer_class = EmployerSerializer
    pagination_class = LimitPageNumberPagination


class CandidateViewset(DjoserUserViewSet):
    """DjoserViewSet кандидата."""

    queryset = User.objects.all().order_by("id")
    serializer_class = CandidateSerializer
    pagination_class = LimitPageNumberPagination


# class OrganizationViewset(viewsets.ModelViewSet):
#     queryset = Organization.objects.all()
#     serializer_class = OrganizationSerializer
#     # permission_classes =
#     pagination_class = LimitPageNumberPagination
#     # filterset_class =


# class CityViewset(viewsets.ModelViewSet):
#     queryset = City.objects.all()
#     serializer_class = CitySerializer
#     # permission_classes =
#     pagination_class = LimitPageNumberPagination
#     # filterset_class =


class SkillViewset(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = (AllowAny,)
    pagination_class = LimitPageNumberPagination
    # filterset_class =
    # filter_backends = (SkillFilter,)


class TrackerViewset(viewsets.ModelViewSet):
    queryset = Tracker.objects.all()
    serializer_class = TrackerSerializer
    # permission_classes =
    pagination_class = LimitPageNumberPagination
    # filterset_class =
    metadata_class = ("get",)

    # @action(detail=False, methods=['GET'],
    #         permission_classes=[IsAuthenticated])
    def get_queryset(self, request, id):
        resume = get_object_or_404(Resume, id=id)
        serializer = TrackerSerializer({"resume": resume.id})
        return response.Response(serializer.data, status=status.HTTP_200_OK)


class ComparisonViewset(viewsets.ModelViewSet):
    queryset = Comparison.objects.all()
    serializer_class = ComparisonSerializer
    # permission_classes = (IsAuthor,)
    pagination_class = LimitPageNumberPagination
    # filterset_class = ComparisonFilter

    @action(
        detail=False,
        methods=(
            "get",
            "post",
            "delete",
        ),
        url_path=r"(?P<vacancy_id>\d+)/comparison",
        permission_classes=[IsAuthenticated],
    )
    def add_to_comparisons(self, request, id):
        resume = get_object_or_404(Resume, id=id)
        serializer = ComparisonSerializer(
            data={"vacancy": request.vacancy.id, "resume": resume.id}
        )
        if request.method == "POST":
            if Comparison.objects.filter(
                resume=resume, vacancy=request.vacancy
            ).exists():
                raise serializers.ValidationError(
                    "Резюме уже есть в Вашем списке подходящих!"
                )
            serializer.is_valid(raise_exception=True)
            serializer.save(vacancy=request.vacancy, resume=resume)
            return response.Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        if request.method == "DELETE":
            comparison = get_object_or_404(
                Comparison, vacancy=request.vacancy, resume__id=id
            )
            comparison.delete()
        return response.Response(
            f"Резюме {comparison.resume} удалено из подходящих."
            f"{request.vacancy}",
            status=status.HTTP_204_NO_CONTENT,
        )

    @action(
        detail=False,
        methods=(
            "get",
            "post",
            "delete",
        ),
        url_path=r"(?P<vacancy_id>\d+)/favorite",
        permission_classes=[IsAuthenticated],
    )
    def add_to_favorites(self, request, id):
        resume = get_object_or_404(Resume, id=id)
        serializer = FavoriteSerializer(
            data={"vacancy": request.vacancy.id, "resume": resume.id}
        )
        if request.method == "POST":
            if Favorite.objects.filter(
                resume=resume, vacancy=request.vacancy
            ).exists():
                raise serializers.ValidationError(
                    "Резюме уже есть в Вашем списке избранных!"
                )
            serializer.is_valid(raise_exception=True)
            serializer.save(vacancy=request.vacancy, resume=resume)
            return response.Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        if request.method == "DELETE":
            favorite = get_object_or_404(
                Favorite, vacancy=request.vacancy, resume__id=id
            )
            favorite.delete()
        return response.Response(
            f"Резюме {favorite.resume} удалено из избранного."
            f"{request.vacancy}",
            status=status.HTTP_204_NO_CONTENT,
        )

    @action(
        detail=False,
        methods=(
            "get",
            "post",
            "delete",
        ),
        url_path=r"(?P<vacancy_id>\d+)/invitation",
        permission_classes=[IsAuthenticated],
    )
    def add_to_invitation(self, request, id):
        resume = get_object_or_404(Resume, id=id)
        serializer = InvitationSerializer(
            data={"vacancy": request.vacancy.id, "resume": resume.id}
        )
        if request.method == "POST":
            if Invitation.objects.filter(
                resume=resume, vacancy=request.vacancy
            ).exists():
                raise serializers.ValidationError(
                    "Данное резюме уже есть в Вашем списке приглашенных!"
                )
            serializer.is_valid(raise_exception=True)
            serializer.save(vacancy=request.vacancy, resume=resume)
            return response.Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        if request.method == "DELETE":
            invitation = get_object_or_404(
                Invitation, vacancy=request.vacancy, resume__id=id
            )
            invitation.delete()
        return response.Response(
            f"Резюме {invitation.resume} удалено из приглашенных."
            f"{request.vacancy}",
            status=status.HTTP_204_NO_CONTENT,
        )


# class FavoriteViewset(viewsets.ModelViewSet):
#     queryset = Favorite.objects.all()
#     serializer_class = FavoriteSerializer
#     # permission_classes =
#     pagination_class = LimitPageNumberPagination
#     # filterset_class =


# class FavoriteViewset(viewsets.ReadOnlyModelViewSet):
#     """Viewset-класс для получение избранных."""

#     queryset = Favorite.objects.all()
#     serializer_class = FavoriteSerializer
#     # permission_classes = должен быть только автор
#     filter_backends = (DjangoFilterBackend,)
#     pagination_class = LimitPageNumberPagination
#     # filterset_fields = ('gender',)  # gender для проверки filter

#     def get_queryset(self):
#         # if self.request.user.is_anonymous:
#         #     # !!!!!!!!!!!!!!!!!! Возможно ли? какое действие? !!!!!!!!!!!!!
#         #     return
# vacancy = get_object_or_404(
#     Vacancy, id=self.kwargs.get("vacancy_id")
# )
#         # if (self.request.user.id == vacancy.author):  # permission
#         #     return
#         ids = Favorite.objects.filter(vacancy_id=vacancy.id).values_list(
#             "resume_id", flat=True
#         )
#         resumes = Resume.objects.filter(id__in=ids)
#         return resumes


# class InvitationViewset(viewsets.ModelViewSet):
#     queryset = Invitation.objects.all()
#     serializer_class = InvitationSerializer
#     # permission_classes =
#     pagination_class = LimitPageNumberPagination
#     # filterset_class =


class ResumeViewset(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    # permission_classes =
    pagination_class = LimitPageNumberPagination
    # filterset_class =

    def get_serializer_class(self):
        if self.request.method in ("POST", "PUT", "PATCH"):
            return ResumeCreateSerializer
        return ResumeInTrackerSerializer


# class SkillInResumeViewset(viewsets.ModelViewSet):
#     queryset = SkillInResume.objects.all()
#     serializer_class = SkillInResumeSerializer
#     # permission_classes =
#     pagination_class = LimitPageNumberPagination
#     # filterset_class =


class VacancyViewset(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    # permission_classes = (IsAuthor,)
    pagination_class = LimitPageNumberPagination
    # filterset_class = VacancyFilter

    def get_serializer_class(self):
        if self.request.method in ("POST", "PUT", "PATCH"):
            return VacancyCreateSerializer
        return VacancyReadListSerializer


# class SkillInVacancyViewset(viewsets.ModelViewSet):
#     queryset = SkillInVacancy.objects.all()
#     serializer_class = SkillInVacancySerializer
#     # permission_classes =
#     pagination_class = LimitPageNumberPagination
#     # filterset_class =
