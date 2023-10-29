from rest_framework import permissions

from vacancy.models import Vacancy


class IsEmployerSelfVacancy(permissions.BasePermission):
    """Права нанимателя входить в свои вакансии."""

    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False
        vacancy_id = request.parser_context["kwargs"].get("vacancy_id")
        if not vacancy_id:
            return False
        vacancy = Vacancy.objects.get(id=vacancy_id)
        return vacancy.author_id == user.id


# class IsEmployer(permissions.BasePermission):
#     """Доступ только нанимателю."""

#     def has_object_permission(self, request, view, obj):
#         return (
#             request.method in permissions.SAFE_METHODS
#             or obj.user == request.employer
#         )


# class IsCandidate(permissions.BasePermission):
#     """Доступ только кандидату."""

#     def has_object_permission(self, request, view, obj):
#         return (
#             request.method in permissions.SAFE_METHODS
#             or obj.user == request.candidate
#         )
