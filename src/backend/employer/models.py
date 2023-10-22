from django.db import models

from user.models import User
from vacancy.models import Vacancy


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
        through='employer.EmployerVacancies',
        to=Vacancy,
    )
    organization = models.ManyToManyField(
        verbose_name="Навыки",
        help_text='Навыки',
        related_name="employers",
        through='employer.EmployerOrganization',
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
