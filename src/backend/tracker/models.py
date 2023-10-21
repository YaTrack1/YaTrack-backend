from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from user.models import Candidate


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
        through='tracker.VacancySkill',
        to=Skill,
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.name


MIN_WEIGHT_SKILL, MAX_WEIGHT_SKILL = 1, 5

class VacancySkill(models.Model):
    """Промежуточная Модель Вакансии и скиллов."""
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


class Resume(models.Model):
    """Модель резюме."""

    class GenderChoices(models.TextChoices):
        MALE = 'M', 'Mуж.'
        FEMALE = 'F', 'Жен.'

    class TypeWorkChoices(models.IntegerChoices):
        UNKNOWN = 0, 'Не известно'
        OFFICE = 1, 'Оффис'
        HYBRID = 2, 'Гибрид'
        REMOTE = 3, 'Удаленка'

    class StatusFinded(models.IntegerChoices):
        UNKNOWN = 0, 'Не известно'
        SEARCH = 1, 'В поиске'
        HOLIDAY = 2, 'В отпуске'
        FOUND = 3, 'Найден'

    candidate = models.OneToOneField(
        Candidate,
        help_text='Кандидат',
        verbose_name='Кандидат',
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='resume',
    )
    # photo = models.ImageField(
    #     "Фото",
    #     upload_to="photo/",
    # )
    gender = models.CharField(
        max_length=1,
        choices=GenderChoices.choices,
        verbose_name='Пол',
        help_text='Пол кандидата',
    )
    city = models.CharField(
        max_length=50,
        verbose_name='Город',
        help_text='Город',
    )
    telegram = models.CharField(
        max_length=50,
        verbose_name='Телеграм',
        help_text='Телеграм',
    )
    github = models.CharField(
        max_length=50,
        verbose_name='GitHub',
        help_text='GitHub',
    )
    about_me = models.TextField(
        verbose_name='О себе',
        help_text='О себе',
    )
    birthday = models.DateField(
        verbose_name='О себе',
        help_text='О себе',
        null=True,
        blank=True,
    )
    status_type_work = models.PositiveSmallIntegerField(
        choices=TypeWorkChoices.choices,
        default=TypeWorkChoices.UNKNOWN,
        verbose_name='Тип работы',
        help_text='Какой устраивает тип работы кандидата',
    )
    status_finded = models.PositiveSmallIntegerField(
        choices=StatusFinded.choices,
        default=StatusFinded.UNKNOWN,
        verbose_name='Статус',
        help_text='Стадия поиска работы кандидата',
    )

    skills = models.ManyToManyField(
        verbose_name="Навыки",
        help_text='Навыки',
        related_name="resume",
        to=Skill,
    )

    class Meta:
        ordering = ['candidate']
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'

    def __str__(self):
        return f'{self.candidate}' if hasattr(self, 'match') else ''
