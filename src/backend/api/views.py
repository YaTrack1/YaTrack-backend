from djoser.views import UserViewSet as DjoserUserViewSet
from rest_framework.viewsets import ReadOnlyModelViewSet
from django.shortcuts import get_object_or_404

from api.serializers import EmployerSerializers, ResumeSerializers
from api.pagination import LimitPageNumberPagination
from resume.models import Resume
from user.models import User
from vacancy.models import Vacancy
from tracker.models import Favorite


class EmployerViewset(DjoserUserViewSet):
    queryset = User.objects.all().order_by("id")
    serializer_class = EmployerSerializers
    pagination_class = LimitPageNumberPagination


class FavoriteViewset(ReadOnlyModelViewSet):
    """Viewset-класс для получение избранных."""
    serializer_class = ResumeSerializers
    # pagination_class = LimitPageNumberPagination
    #permission_classes = должен быть только автор

    def get_queryset(self):
        print(self.request.user)
        print(self.request.user.id)
        # if self.request.user.is_anonymous:
        #     # !!!!!!!!!!!!!!!!!! Возможно ли? какое действие? !!!!!!!!!!!!!!!!
        #     return
        vacancy = get_object_or_404(
            Vacancy,
            id=self.kwargs.get('vacancy_id')
        )
        # if (self.request.user.id == vacancy.author):  # permission
        #     return
        ids = (Favorite.objects
               .filter(vacancy_id=vacancy.id)
               .values_list('resume_id', flat=True))
        print(vacancy.id, ids)
        resumes = Resume.objects.filter(id__in=ids)
        print(resumes)
        return resumes
