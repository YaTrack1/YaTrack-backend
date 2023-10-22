from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from user.models import User


class Employer(User):

    date_create = models.DateTimeField()

    class Meta:
        verbose_name = "Наниматель"
        verbose_name_plural = "Наниматели"
        default_related_name = "employers"


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

    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Название",
        help_text="Название города",
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return self.name


class Skill(models.Model):
    """Модель тегов."""

    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Название",
        help_text="Название навыка",
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    """Модель Вакансии."""

    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Название",
        help_text="Название вакансии",
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Описание вакансии",
        null=True,
        blank=True,
    )
    skills = models.ManyToManyField(
        verbose_name="Навыки",
        help_text="Навыки",
        related_name="vacancies",
        through="tracker.VacancySkill",
        to=Skill,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return self.name


class VacancySkill(models.Model):
    """Промежуточная Модель Вакансии и скиллов."""

    MIN_WEIGHT_SKILL, MAX_WEIGHT_SKILL = 1, 5
    vacancy = models.ForeignKey(
        verbose_name="Вакансии",
        help_text="В каких вакансиях",
        related_name="skill",
        to=Vacancy,
        on_delete=models.CASCADE,
    )
    skill = models.ForeignKey(
        verbose_name="Навыки",
        help_text="Связанный навык",
        related_name="vacancy",
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
                    "vacancy",
                    "skill",
                ),
                name="unique_vacancy_skill",
            ),
        )

    def __str__(self):
        return f"{self.skill}({self.vacancy}) - {self.weight}"


class Resume(models.Model):
    """Модель резюме."""

    class GenderChoices(models.TextChoices):
        MALE = "M", "Mуж."
        FEMALE = "F", "Жен."

    class TypeWorkChoices(models.IntegerChoices):
        UNKNOWN = 0, "Не известно"
        OFFICE = 1, "Оффис"
        HYBRID = 2, "Гибрид"
        REMOTE = 3, "Удаленка"

    class StatusFinded(models.IntegerChoices):
        UNKNOWN = 0, "Не известно"
        SEARCH = 1, "В поиске"
        HOLIDAY = 2, "В отпуске"
        FOUND = 3, "Найден"

    candidate = models.ForeignKey(
        Candidate,
        help_text="Кандидат",
        verbose_name="Кандидат",
        on_delete=models.CASCADE,
        related_name="resume",
    )
    # photo = models.ImageField(
    #     "Фото",
    #     upload_to="photo/",
    # )
    gender = models.CharField(
        max_length=1,
        choices=GenderChoices.choices,
        verbose_name="Пол",
        help_text="Пол кандидата",
    )
    city = models.ForeignKey(
        City,
        help_text="Город кондидата",
        verbose_name="Город",
        on_delete=models.CASCADE,
        related_name="candidate",
    )
    telegram = models.CharField(
        max_length=50,
        verbose_name="Телеграм",
        help_text="Телеграм",
    )
    github = models.CharField(
        max_length=50,
        verbose_name="GitHub",
        help_text="GitHub",
    )
    about_me = models.TextField(
        verbose_name="О себе",
        help_text="О себе",
    )
    birthday = models.DateField(
        verbose_name="День рождения",
        help_text="День рождкния",
        null=True,
        blank=True,
    )
    status_type_work = models.PositiveSmallIntegerField(
        choices=TypeWorkChoices.choices,
        default=TypeWorkChoices.UNKNOWN,
        verbose_name="Тип работы",
        help_text="Какой устраивает тип работы кандидата",
    )
    status_finded = models.PositiveSmallIntegerField(
        choices=StatusFinded.choices,
        default=StatusFinded.UNKNOWN,
        verbose_name="Статус",
        help_text="Стадия поиска работы кандидата",
    )
    skills = models.ManyToManyField(
        verbose_name="Навыки",
        help_text="Навыки",
        related_name="resumes",
        through="tracker.ResumeSkill",
        to=Skill,
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
