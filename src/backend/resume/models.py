from django.db import models

from user.models import Candidate
from vacancy.models import Skill


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
        ordering = ["candidate"]
        verbose_name = "Резюме"
        verbose_name_plural = "Резюме"

    def __str__(self):
        return f"{self.candidate}" if hasattr(self, "match") else ""


class ResumeSkill(models.Model):
    """Промежуточная Модель резюме и скиллов."""

    resume = models.ForeignKey(
        verbose_name="Резюме",
        help_text="В каких резюме",
        related_name="skill",
        to=Resume,
        on_delete=models.CASCADE,
    )
    skill = models.ForeignKey(
        verbose_name="Навыки",
        help_text="Связанный навык",
        related_name="resume",
        to=Skill,
        on_delete=models.CASCADE,
    )
    level = models.PositiveSmallIntegerField(
        verbose_name="Уровень",
        help_text="Уровень навыка",
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
        return f"{self.skill}({self.resume}) - {self.level}"
