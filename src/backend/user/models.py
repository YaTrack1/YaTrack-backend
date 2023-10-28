import re
import unicodedata

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from .validators import username_validator


class User(AbstractUser):
    username = models.CharField(
        "Логин",
        max_length=settings.MAX_LENGTH,
        unique=True,
        blank=False,
        validators=[
            RegexValidator(regex=settings.CHAR_VALID_USER),
            username_validator,
        ],
        help_text=(settings.LENGTH_HELP),
    )
    password = models.CharField(
        "Пароль",
        max_length=settings.MAX_LENGTH,
        blank=False,
        null=False,
        help_text=(settings.LENGTH_HELP),
    )
    email = models.EmailField(
        "Адрес электронной почты",
        max_length=settings.MAIL_LENGTH,
        unique=True,
        blank=False,
        help_text=(settings.LENGTH_HELP),
    )
    first_name = models.CharField(
        "Имя",
        max_length=settings.MAX_LENGTH,
        blank=False,
        validators=[
            RegexValidator(regex=settings.CHAR_VALID),
            username_validator,
        ],
        help_text=(settings.LENGTH_HELP),
    )
    last_name = models.CharField(
        "Фамилия",
        max_length=settings.MAX_LENGTH,
        blank=False,
        validators=[
            RegexValidator(regex=settings.CHAR_VALID),
            username_validator,
        ],
        help_text=(settings.LENGTH_HELP),
    )

    last_visited = models.DateTimeField(
        verbose_name="Последний визит",
        auto_now_add=False,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username

    @classmethod
    def normalize_email(cls, email: str):
        if not isinstance(email, str) or not re.match(
            settings.MAIL_VALID, email
        ):
            raise ValueError(settings.MAIL_ERROR.format(email))
        email_name, domain_part = email.strip().rsplit("@", 1)
        return email_name.lower() + "@" + domain_part.lower()

    @classmethod
    def normalize_username(cls, username: str):
        return unicodedata.normalize("NFKC", username).capitalize()

    def __normalize_human_names(self, name: str):
        return " ".join([word.capitalize() for word in name.split()])

    def clean(self) -> None:
        self.first_name = self.__normalize_human_names(self.first_name)
        self.last_name = self.__normalize_human_names(self.last_name)
        super().clean()
