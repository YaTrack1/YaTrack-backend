from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class NameModel(models.Model):
    """Модель, которая имеет лишь название."""

    name = models.CharField(
        verbose_name="Название",
        max_length=50,
        unique=True,
        primary_key=True,
    )


class Skill(NameModel):
    """Модель Навыков."""

    class Meta:
        ordering = ["name"]
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"

    def __str__(self):
        return self.name


class Vacancy(NameModel):
    """Модель Вакансии."""

    description = models.TextField(
        verbose_name="Описание",
        help_text="Описание вакансии",
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return self.name


class JobTitle(NameModel):
    skills = models.ManyToManyField(
        verbose_name="Навыки",
        related_name="job_titles",
        through="JobSkill",
        to=Skill,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Должность"
        verbose_name_plural = "Должности"


class JobSkill(models.Model):
    """Промежуточная Модель Должности и скиллов."""

    MIN_WEIGHT_SKILL, MAX_WEIGHT_SKILL = 1, 5
    job_title = models.ForeignKey(
        verbose_name="Должность",
        related_name="skill",
        to=JobTitle,
        on_delete=models.CASCADE,
    )
    skill = models.ForeignKey(
        verbose_name="Навыки",
        related_name="job_title",
        to=Skill,
        on_delete=models.CASCADE,
    )
    weight = models.PositiveSmallIntegerField(
        verbose_name="Вес",
        help_text="Важность навыка",
        default=MIN_WEIGHT_SKILL,
        validators=(
            MinValueValidator(
                MIN_WEIGHT_SKILL,
                f"Как минимум {MIN_WEIGHT_SKILL}",
            ),
            MaxValueValidator(
                MAX_WEIGHT_SKILL,
                f"Как максимум {MAX_WEIGHT_SKILL}",
            ),
        ),
    )

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"
        constraints = (
            models.UniqueConstraint(
                fields=(
                    "job_title",
                    "skill",
                ),
                name="unique_job_skill",
            ),
        )

    def __str__(self):
        return f"{self.skill}({self.job_title}) - {self.weight}"
