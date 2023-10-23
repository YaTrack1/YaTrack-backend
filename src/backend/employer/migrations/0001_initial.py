# Generated by Django 4.2.6 on 2023-10-23 00:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("vacancy", "__first__"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Organization",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Название организации",
                        max_length=50,
                        unique=True,
                        verbose_name="Название",
                    ),
                ),
                (
                    "itn",
                    models.CharField(
                        blank=True,
                        help_text="Идентификационный номер налогоплательщика",
                        max_length=50,
                        null=True,
                        unique=True,
                        verbose_name="ИНН",
                    ),
                ),
            ],
            options={
                "verbose_name": "Навык",
                "verbose_name_plural": "Навыки",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="EmployerVacancies",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "employer",
                    models.ForeignKey(
                        help_text="Наниматель",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="vacancy",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Наниматель",
                    ),
                ),
                (
                    "vacancy",
                    models.ForeignKey(
                        help_text="Связанная вакансия с нанимателем",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="employer",
                        to="vacancy.vacancy",
                        verbose_name="Вакансии",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EmployerOrganization",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "employer",
                    models.ForeignKey(
                        help_text="Наниматель",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="organizations",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Наниматель",
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        help_text="Связанная организация с нанимателем",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="employer",
                        to="employer.organization",
                        verbose_name="Организация",
                    ),
                ),
            ],
        ),
    ]
