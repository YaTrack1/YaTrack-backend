from django.db import models

# from user.models import User
# from vacancy.models import Vacancy


class NameModel(models.Model):
    """Модель, которая имеет лишь название."""

    name = models.CharField(
        verbose_name="Название",
        max_length=50,
        unique=True,
        primary_key=True,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class City(NameModel):
    """Модель городов"""

    class Meta:
        ordering = ["name"]
        verbose_name = "Город"
        verbose_name_plural = "Города"


class Skill(NameModel):
    """Модель Навыков."""

    class Meta:
        ordering = ["name"]
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"


class Organization(NameModel):
    """Модель организации нанимателей."""

    itn = models.CharField(
        max_length=50,
        unique=True,
        null=False,
        blank=True,
        verbose_name="ИНН",
        help_text="Идентификационный номер налогоплательщика",
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"


# class EmployerOrganization(models.Model):
#     """Таблица наниматели - их представительство в организации."""
#     employer = models.ForeignKey(
#         verbose_name="Наниматель",
#         help_text='Наниматель',
#         related_name="organizations",
#         to=User,
#         on_delete=models.CASCADE,
#     )
#     organization = models.ForeignKey(
#         verbose_name="Организация",
#         help_text='Связанная организация с нанимателем',
#         related_name="employer",
#         to=Organization,
#         on_delete=models.CASCADE,
#     )


# class EmployerVacancies(models.Model):
#     """Таблица наниматели - vacancy"""
#     employer = models.ForeignKey(
#         verbose_name="Наниматель",
#         help_text='Наниматель',
#         related_name="vacancy",
#         to=User,
#         on_delete=models.CASCADE,
#     )
#     vacancy = models.ForeignKey(
#         verbose_name="Вакансии",
#         help_text='Связанная вакансия с нанимателем',
#         related_name="employer",
#         to=Vacancy,
#         on_delete=models.CASCADE,
#     )
