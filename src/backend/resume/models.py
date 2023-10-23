from django.db import models
from django.conf import settings

from user.models import User
from core.models import Skill

# City


# class Candidate(User):
#     last_visit = models.DateTimeField(
#         "Последнее время онлайна",
#         auto_now_add=True,
#     )

#     birthday = models.DateField("День рождения")
#     date_create = models.DateTimeField(default=settings.DATETIME_NOW)

#     class Meta:
#         verbose_name = "Кандидат"
#         verbose_name_plural = "Кандидаты"
#         default_related_name = "candidates"
#         ordering = ("username",)


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
    city = models.CharField(verbose_name="Город")
    telegram = models.CharField(
        max_length=50,
        verbose_name="Телеграм",
    )
    github = models.CharField(
        max_length=50,
        verbose_name="GitHub",
    )
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
        return f"{self.candidate}" if hasattr(self, "match") else ""


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


# class ResumeSkill(models.Model):
#     """Промежуточная Модель резюме и скиллов."""

#     resume = models.ForeignKey(
#         verbose_name="Резюме",
#         help_text="В каких резюме",
#         related_name="skill",
#         to=Resume,
#         on_delete=models.CASCADE,
#     )
#     skill = models.ForeignKey(
#         verbose_name="Навыки",
#         help_text="Связанный навык",
#         related_name="resume",
#         to=Skill,
#         on_delete=models.CASCADE,
#     )
#     level = models.PositiveSmallIntegerField(
#         verbose_name="Уровень",
#         help_text="Уровень навыка",
#         default=1,  # ???
#         # validators=(
#         #     MinValueValidator(
#         #         MIN_WEIGHT_SKILL,
#         #         f'Как минимум {MIN_WEIGHT_SKILL}',
#         #     ),
#         #     MaxValueValidator(
#         #         MAX_WEIGHT_SKILL,
#         #         f'Как максимум {MAX_WEIGHT_SKILL}',
#         #     ),
#         # ),
#     )

#     class Meta:
#         verbose_name = "Навык"
#         verbose_name_plural = "Навыки"
#         constraints = (
#             models.UniqueConstraint(
#                 fields=(
#                     "resume",
#                     "skill",
#                 ),
#                 name="unique_resume_skill",
#             ),
#         )

#     def __str__(self):
#         return f"{self.skill}({self.resume}) - {self.level}"
