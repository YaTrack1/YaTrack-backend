from django.db import models
from django.conf import settings

from user.models import User
from core.models import City, Skill


class Vacancy(models.Model):
    """Модель Вакансии."""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Наниматель",
    )
    position = models.CharField(
        "Должность",
        max_length=settings.MAX_LENGTH,
    )
    specialty = models.CharField(
        "Специализация",
        max_length=settings.MAX_LENGTH,
    )
    description = models.TextField(
        verbose_name="Описание",
        null=True,
        blank=True,
    )
    duties = models.CharField(
        "Обязанности",
        max_length=settings.MAX_LENGTH,
    )
    city = models.ForeignKey(
        City, on_delete=models.SET_NULL, null=True, verbose_name="Город"
    )
    conditions = models.CharField(
        "Условия",
        max_length=settings.MAX_LENGTH,
    )
    stages = models.CharField(
        "Этапы отбора",
        max_length=settings.MAX_LENGTH,
    )

    class Meta:
        ordering = ["position"]
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"
        default_related_name = "vacancys"

    def __str__(self):
        return self.position


class SkillInVacancy(models.Model):
    skill = models.ForeignKey(
        Skill,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Скилл",
        related_name="+",
    )
    vacancy = models.ForeignKey(
        Vacancy,
        on_delete=models.CASCADE,
        verbose_name="Вакансия",
        related_name="skill_list",
    )

    importance = models.PositiveSmallIntegerField(
        verbose_name="Важность навыка",
        default=0,
    )

    class Meta:
        ordering = ("vacancy",)
        verbose_name = "Скилл в вакансии"
        verbose_name_plural = "Скилы в вакансии"
        constraints = (
            models.UniqueConstraint(
                fields=(
                    "skill",
                    "vacancy",
                ),
                name="unique_skill_vacancy",
            ),
        )

    def __str__(self):
        return f"{self.skill} в {self.vacancy}"
