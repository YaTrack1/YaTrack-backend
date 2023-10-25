import django_filters

from resume.models import Resume
from user.models import Subscription, User
from vacancy.models import Vacancy
from tracker.models import Favorite


class SelectionResumesFilter(django_filters.FilterSet):
    """Фильтр для выбора резюме."""
    actived = django_filters.BooleanFilter(
        field_name='candidate__is_active',
    )
    # /?actived=true
    is_favorite_from = django_filters.BooleanFilter(
        field_name='candidate',
        method='get_is_favorite_from_candidate',
    )
    # /api/tracker/3/favorite/?is_favorite_from=true
    is_favorite = django_filters.BooleanFilter(
        field_name='vacancy',
        method='get_is_favorite_candidate',
    )
    # /api/tracker/3/favorite/?is_favorite=true
    email = django_filters.CharFilter(lookup_expr='contains')
    city = django_filters.CharFilter(lookup_expr='contains')
    about_me = django_filters.CharFilter(lookup_expr='contains')
    birthday__gte = django_filters.NumberFilter(
        field_name='birthday',
        lookup_expr='year__gte',
    )
    # /?birthday__gte=1992  - больше и равно дня рождения
    birthday__lte = django_filters.NumberFilter(
        field_name='birthday',
        lookup_expr='year__lte',
    )
    candidate = django_filters.CharFilter(
        field_name='candidate__username',
        lookup_expr='contains',
    )

    def get_is_favorite_from_candidate(self, queryset, name, value):
        user = self.request.user
        if user.is_anonymous:
            return queryset
        candidate_ids = Subscription.objects.filter(
            employer_id=user.id).values_list('candidate_id', flat=True)
        candidate_ids = User.objects.filter(
            id__in=candidate_ids).values_list('id', flat=True)
        resumes = Resume.objects.filter(candidate_id__in=candidate_ids)
        return resumes

    def get_is_favorite_candidate(self, queryset, name, value):
        request = self.request
        user = request.user
        if user.is_anonymous:
            return queryset
        vacancy_id = request.parser_context['kwargs'].get('vacancy_id')
        if not vacancy_id:
            return queryset
        vacancies = Vacancy.objects.filter(id=vacancy_id)
        if not vacancies.count():
            return queryset
        vacancy = vacancies.first()
        ids = Favorite.objects.filter(vacancy_id=vacancy.id).values_list(
            "resume_id", flat=True
        )
        resumes = Resume.objects.filter(id__in=ids)
        return resumes

    class Meta:
        model = Resume
        fields = []
        # fields = ('email', 'city', 'birthday', )
