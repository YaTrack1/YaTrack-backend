from django.db import models
from django.conf import settings

from vacancy.models import Vacancy
from resume.models import Resume
from user.models import User


class Tracker(models.Model):
    """Модель трекера всех резюме."""

    resume = models.ForeignKey(
        Resume, on_delete=models.CASCADE, verbose_name="Резюме"
    )

    class Meta:
        verbose_name = "Трекер"
        verbose_name_plural = "Трекер"

    def __str__(self):
        return "self.resume" if hasattr(self, "resume") else " "


class ResumeInVacancy(models.Model):
    """Абстрактная модель резюме в вакансии."""

    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        verbose_name="Резюме",
    )
    vacancy = models.ForeignKey(
        Vacancy,
        on_delete=models.CASCADE,
        verbose_name="Вакансия",
        related_name="+",
    )

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.resume} из {self.vacancy}"


class Comparison(ResumeInVacancy):
    """Модель подходящих кандидатов по резюме."""

    class Meta:
        verbose_name = "Сравнение подходящих вакансий"
        verbose_name_plural = "Сравнения подходящих вакансий"
        default_related_name = "comparisons"
        constraints = (
            models.UniqueConstraint(
                fields=(
                    "vacancy",
                    "resume",
                ),
                name="unique_comparison_resume",
            ),
        )


class Favorite(ResumeInVacancy):
    """Модель избранных кандидатов по резюме."""

    class Meta:
        verbose_name = "Избранный"
        verbose_name_plural = "Избранные"
        default_related_name = "favorites"
        constraints = (
            models.UniqueConstraint(
                fields=(
                    "vacancy",
                    "resume",
                ),
                name="unique_favorite_resume",
            ),
        )


class Interested(ResumeInVacancy):
    """Модель заинтересованный кандидат относительно вакансии."""

    class Meta:
        verbose_name = "Заинтерисованный"
        verbose_name_plural = "Заинтересованные"
        default_related_name = "interested"
        constraints = (
            models.UniqueConstraint(
                fields=(
                    "vacancy",
                    "resume",
                ),
                name="unique_interested_resume",
            ),
        )


class Invitation(ResumeInVacancy):
    """Модель приглашенных кандидатов по резюме."""

    status = models.PositiveSmallIntegerField(
        choices=settings.STATUS_INVITATION,
        default=settings.ZERO,
        verbose_name="Статус",
    )

    class Meta:
        verbose_name = "Приглашенный"
        verbose_name_plural = "Приглашенные"
        default_related_name = "invitations"
        constraints = (
            models.UniqueConstraint(
                fields=(
                    "vacancy",
                    "resume",
                ),
                name="unique_invitation_resume",
            ),
        )


class UserViewedResume(models.Model):
    """Модель пользователь просмотрел резюме."""

    employer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Вакансия",
        related_name="resume",
    )
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        verbose_name="Резюме",
        related_name="employers",
    )

    class Meta:
        verbose_name = "Просмотр"
        verbose_name_plural = "Просмотры"
        constraints = (
            models.UniqueConstraint(
                fields=(
                    "employer",
                    "resume",
                ),
                name="unique_employer_resume",
            ),
        )

    def __str__(self):
        return f"{self.employer} просмотрел {self.resume}"
