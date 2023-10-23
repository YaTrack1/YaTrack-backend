from django.db import models

# from django.core.validators import MaxValueValidator, MinValueValidator

from user.models import User
from core.models import City, Skill


class Vacancy(models.Model):
    """Модель Вакансии."""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Наниматель",
    )
    position = models.CharField("Должность")
    specialty = models.CharField("Специализация")
    description = models.TextField(
        verbose_name="Описание",
        null=True,
        blank=True,
    )
    duties = models.CharField("Обязанности")
    city = models.ForeignKey(
        City, on_delete=models.SET_NULL, null=True, verbose_name="Город"
    )
    conditions = models.CharField("Условия")
    stages = models.CharField("Этапы отбора")

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


# class JobTitle(NameModel):
#     skills = models.ManyToManyField(
#         verbose_name="Навыки",
#         related_name="job_titles",
#         through="JobSkill",
#         to=Skill,
#     )

#     class Meta:
#         ordering = ["name"]
#         verbose_name = "Должность"
#         verbose_name_plural = "Должности"


# class JobSkill(models.Model):
#     """Промежуточная Модель Должности и скиллов."""

#     MIN_WEIGHT_SKILL, MAX_WEIGHT_SKILL = 1, 5
#     job_title = models.ForeignKey(
#         verbose_name="Должность",
#         related_name="skill",
#         to=JobTitle,
#         on_delete=models.CASCADE,
#     )
#     skill = models.ForeignKey(
#         verbose_name="Навыки",
#         related_name="job_title",
#         to=Skill,
#         on_delete=models.CASCADE,
#     )
#     weight = models.PositiveSmallIntegerField(
#         verbose_name="Вес",
#         help_text="Важность навыка",
#         default=MIN_WEIGHT_SKILL,
#         validators=(
#             MinValueValidator(
#                 MIN_WEIGHT_SKILL,
#                 f"Как минимум {MIN_WEIGHT_SKILL}",
#             ),
#             MaxValueValidator(
#                 MAX_WEIGHT_SKILL,
#                 f"Как максимум {MAX_WEIGHT_SKILL}",
#             ),
#         ),
#     )

#     class Meta:
#         verbose_name = "Навык"
#         verbose_name_plural = "Навыки"
#         constraints = (
#             models.UniqueConstraint(
#                 fields=(
#                     "job_title",
#                     "skill",
#                 ),
#                 name="unique_job_skill",
#             ),
#         )

#     def __str__(self):
#         return f"{self.skill}({self.job_title}) - {self.weight}"
