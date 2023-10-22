from django.db import models

from user.models import User
from vacancy.models import Skill, Vacancy


class Organization(models.Model):
    """Модель организации нанимателей."""
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Название',
        help_text='Название организации',
    )
    itn = models.CharField(
        max_length=50,
        unique=True,
        null=True,
        blank=True,
        verbose_name='ИНН',
        help_text='Идентификационный номер налогоплательщика',
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return self.name


class Employer(User):
    """Модельн нанимателя."""
    vacancies = models.ManyToManyField(
        verbose_name="Навыки",
        help_text='Навыки',
        related_name="employers",
        through='tracker.EmployerVacancies',
        to=Vacancy,
    )
    organization = models.ManyToManyField(
        verbose_name="Навыки",
        help_text='Навыки',
        related_name="employers",
        through='tracker.EmployerOrganization',
        to=Organization,
    )

    class Meta:
        verbose_name = "Наниматель"
        verbose_name_plural = "Наниматели"


class EmployerOrganization(models.Model):
    """Таблица наниматели - их представительство в организации."""
    employer = models.ForeignKey(
        verbose_name="Наниматель",
        help_text='Наниматель',
        related_name="organizations",
        to=Employer,
        on_delete=models.CASCADE,
    )
    organization = models.ForeignKey(
        verbose_name="Организация",
        help_text='Связанная организация с нанимателем',
        related_name="employer",
        to=Organization,
        on_delete=models.CASCADE,
    )


class EmployerVacancies(models.Model):
    """Таблица наниматели - vacancy"""
    employer = models.ForeignKey(
        verbose_name="Наниматель",
        help_text='Наниматель',
        related_name="vacancy",
        to=Employer,
        on_delete=models.CASCADE,
    )
    vacancy = models.ForeignKey(
        verbose_name="Вакансии",
        help_text='Связанная вакансия с нанимателем',
        related_name="employer",
        to=Vacancy,
        on_delete=models.CASCADE,
    )


class Candidate(User):
    last_visit = models.DateTimeField(
        "Последнее время онлайна",
        auto_now_add=True,
    )

    birthday = models.DateField("День рождения")
    date_create = models.DateTimeField()

    class Meta:
        verbose_name = "Кандидат"
        verbose_name_plural = "Кандидаты"
        default_related_name = "candidates"
        ordering = ("username",)


class City(models.Model):
    """Модель городов"""
    name = models.CharField(max_length=50,
                            unique=True,
                            verbose_name='Название',
                            help_text='Название города',)

    class Meta:
        ordering = ['name']
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name


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

    candidate = models.ForeignKey(
        Candidate,
        help_text='Кандидат',
        verbose_name='Кандидат',
        on_delete=models.CASCADE,
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
    city = models.ForeignKey(
        City,
        help_text='Город кондидата',
        verbose_name='Город',
        on_delete=models.CASCADE,
        related_name='candidate',
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
        verbose_name='День рождения',
        help_text='День рождкния',
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
        related_name="resumes",
        through='tracker.ResumeSkill',
        to=Skill,
    )

    class Meta:
        ordering = ['candidate']
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'

    def __str__(self):
        return f'{self.candidate}' if hasattr(self, 'match') else ''


class ResumeSkill(models.Model):
    """Промежуточная Модель резюме и скиллов."""
    resume = models.ForeignKey(
        verbose_name="Резюме",
        help_text='В каких резюме',
        related_name="skill",
        to=Resume,
        on_delete=models.CASCADE,
    )
    skill = models.ForeignKey(
        verbose_name="Навыки",
        help_text='Связанный навык',
        related_name="resume",
        to=Skill,
        on_delete=models.CASCADE,
    )
    level = models.PositiveSmallIntegerField(
        verbose_name='Уровень',
        help_text='Уровень навыка',
        default=1,  # ???
        # validators=(
        #     MinValueValidator(
        #         MIN_WEIGHT_SKILL,
        #         f'Как минимум {MIN_WEIGHT_SKILL}',
        #     ),
        #     MaxValueValidator(
        #         MAX_WEIGHT_SKILL,
        #         f'Как максимум {MAX_WEIGHT_SKILL}',
        #     ),
        # ),
    )

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"
        constraints = (
            models.UniqueConstraint(
                fields=(
                    "resume",
                    "skill",
                ),
                name="unique_resume_skill",
            ),
        )

    def __str__(self):
        return f'{self.skill}({self.resume}) - {self.level}'
