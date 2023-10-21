from djoser.views import UserViewSet as DjoserUserViewSet

from user.models import User
from api.serializers import EmployerSerializers
from api.pagination import LimitPageNumberPagination


class EmployerViewset(DjoserUserViewSet):
    queryset = User.objects.all().order_by("id")
    serializer_class = EmployerSerializers
    pagination_class = LimitPageNumberPagination
