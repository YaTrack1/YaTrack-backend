from django.conf import settings
from django.core.exceptions import ValidationError


def username_validator(username):
    if username == "me":
        raise ValidationError(settings.USER_VALID.format(username))
    return username
