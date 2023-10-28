from datetime import date

from django.db import models
from django.conf import settings

from user.models import User
from core.models import Skill


class Resume(models.Model):
    """Модель резюме."""

    title = models.CharField("Заголовок")
    candidate = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Кандидат",
    )
    photo = models.ImageField(
        "Фото",
        upload_to="photo/",
        default=None,
    )
    gender = models.CharField(
        max_length=1,
        choices=settings.GENDER_FLAG,
        verbose_name="Пол",
    )
    # city = models.ForeignKey(
    #     City,
    #     on_delete=models.SET_NULL,
    #     verbose_name="Город",
    # )
    # grade = models.CharField("Грейд")
    city = models.CharField(verbose_name="Город")
    telegram = models.CharField(
        max_length=50,
        verbose_name="Телеграм",
    )
    github = models.CharField(
        max_length=50,
        verbose_name="GitHub",
    )
    portfolio = models.CharField(verbose_name="Портфолио")
    about_me = models.TextField(
        verbose_name="О себе",
    )
    birthday = models.DateField(
        verbose_name="День рождения",
        null=True,
        blank=True,
    )
    status_type_work = models.PositiveSmallIntegerField(
        choices=settings.TYPE_WORK,
        default=settings.ZERO,
        verbose_name="Тип работы",
    )
    status_finded = models.PositiveSmallIntegerField(
        choices=settings.STATUS_FIDED,
        default=settings.ZERO,
        verbose_name="Статус",
    )
    date_created = models.DateTimeField(
        verbose_name="Создание резюме",
        auto_now=True,
    )
    # skills = models.ManyToManyField(
    #     verbose_name="Навыки",
    #     related_name="resumes",
    #     to=Skill,
    # )

    class Meta:
        ordering = ["candidate"]
        verbose_name = "Резюме"
        verbose_name_plural = "Резюме"
        default_related_name = "resumes"

    def __str__(self):
        return f"{self.candidate}" if hasattr(self, "candidate") else ""

    def get_age(self) -> int:
        """Получить возраст кандидата."""
        return (date.today() - self.birthday).year

    get_age.short_description = "Возраст"


class SkillInResume(models.Model):
    skill = models.ForeignKey(
        Skill,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Скилл",
        related_name="+",
    )
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        verbose_name="Резюме",
        related_name="skill_list",
    )
    rating = models.PositiveSmallIntegerField(
        verbose_name="Рейтинг навыка",
        default=0,
    )

    class Meta:
        ordering = ("resume",)
        verbose_name = "Скилл в резюме"
        verbose_name_plural = "Скиллы в резюме"
        constraints = (
            models.UniqueConstraint(
                fields=(
                    "skill",
                    "resume",
                ),
                name="unique_skill_resume",
            ),
        )

    def __str__(self):
        return f"{self.skill} в {self.resume}"


class Experience(models.Model):
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        verbose_name="Опыт",
        related_name="experiences",
    )

    position = models.CharField(verbose_name="Позиция")
    period = models.CharField(verbose_name="Период")
    duties = models.TextField(
        verbose_name="Обязанности",
    )

    class Meta:
        verbose_name = "Опыт"
        verbose_name_plural = "Опыты"

    def __str__(self):
        return f"{self.position}"


class Education(models.Model):
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        verbose_name="Образование",
        related_name="educations",
    )

    grade = models.CharField(verbose_name="Уровень образования")
    institution = models.CharField(verbose_name="Университет")
    period = models.CharField(verbose_name="Период")
    speciality = models.CharField(
        verbose_name="Специальность",
    )

    class Meta:
        verbose_name = "Образование"
        verbose_name_plural = "Образования"

    def __str__(self):
        return f"{self.institution}"
