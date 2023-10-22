from django.db import models

from vacancy.models import Vacancy
from resume.models import Resume


class Tracker(models.Model):
    resume = models.ForeignKey(
        Resume, on_delete=models.CASCADE, verbose_name="Резюме"
    )

    def __str__(self):
        return self.resume


class ResumeInVacancy(models.Model):
    resume = models.ForeignKey(
        Resume, on_delete=models.CASCADE, verbose_name="Резюме"
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


class Invitation(ResumeInVacancy):
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
