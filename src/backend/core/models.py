from django.db import models


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
        ordering = ("name",)
        verbose_name = "Город"
        verbose_name_plural = "Города"


class Skill(NameModel):
    """Модель Навыков."""

    class Meta:
        ordering = ("name",)
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
        ordering = ("name",)
        verbose_name = "Организация"
        verbose_name_plural = "Организации"
