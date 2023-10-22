from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Skill(models.Model):
    """Модель тегов."""
    name = models.CharField(max_length=50,
                            unique=True,
                            verbose_name='Название',
                            help_text='Название навыка', )

    class Meta:
        ordering = ['name']
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    """Модель Вакансии."""
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Название',
        help_text='Название вакансии',
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Описание вакансии',
        null=True,
        blank=True,
    )
    skills = models.ManyToManyField(
        verbose_name="Навыки",
        help_text='Навыки',
        related_name="vacancies",
        through='vacancy.VacancySkill',
        to=Skill,
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.name


class VacancySkill(models.Model):
    """Промежуточная Модель Вакансии и скиллов."""
    MIN_WEIGHT_SKILL, MAX_WEIGHT_SKILL = 1, 5
    vacancy = models.ForeignKey(
        verbose_name="Вакансии",
        help_text='В каких вакансиях',
        related_name="skill",
        to=Vacancy,
        on_delete=models.CASCADE,
    )
    skill = models.ForeignKey(
        verbose_name="Навыки",
        help_text='Связанный навык',
        related_name="vacancy",
        to=Skill,
        on_delete=models.CASCADE,
    )
    weight = models.PositiveSmallIntegerField(
        verbose_name="Вес",
        help_text='Важность навыка',
        default=MIN_WEIGHT_SKILL,
        validators=(
            MinValueValidator(
                MIN_WEIGHT_SKILL,
                f'Как минимум {MIN_WEIGHT_SKILL}',
            ),
            MaxValueValidator(
                MAX_WEIGHT_SKILL,
                f'Как максимум {MAX_WEIGHT_SKILL}',
            ),
        ),
    )

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"
        constraints = (
            models.UniqueConstraint(
                fields=(
                    "vacancy",
                    "skill",
                ),
                name="unique_vacancy_skill",
            ),
        )

    def __str__(self):
        return f'{self.skill}({self.vacancy}) - {self.weight}'

