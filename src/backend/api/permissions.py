# from rest_framework import permissions


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
