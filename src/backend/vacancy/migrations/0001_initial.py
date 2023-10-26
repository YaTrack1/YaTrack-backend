# Generated by Django 4.2.6 on 2023-10-26 01:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("core", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Vacancy",
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
                ("position", models.CharField(verbose_name="Должность")),
                ("specialty", models.CharField(verbose_name="Специализация")),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Описание"
                    ),
                ),
                ("duties", models.CharField(verbose_name="Обязанности")),
                ("conditions", models.CharField(verbose_name="Условия")),
                ("stages", models.CharField(verbose_name="Этапы отбора")),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Наниматель",
                    ),
                ),
                (
                    "city",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="core.city",
                        verbose_name="Город",
                    ),
                ),
            ],
            options={
                "verbose_name": "Вакансия",
                "verbose_name_plural": "Вакансии",
                "ordering": ["position"],
                "default_related_name": "vacancys",
            },
        ),
        migrations.CreateModel(
            name="SkillInVacancy",
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
                    "skill",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="core.skill",
                        verbose_name="Скилл",
                    ),
                ),
                (
                    "vacancy",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="skill_list",
                        to="vacancy.vacancy",
                        verbose_name="Вакансия",
                    ),
                ),
            ],
            options={
                "verbose_name": "Скилл в вакансии",
                "verbose_name_plural": "Скилы в вакансии",
                "ordering": ("vacancy",),
            },
        ),
        migrations.AddConstraint(
            model_name="skillinvacancy",
            constraint=models.UniqueConstraint(
                fields=("skill", "vacancy"), name="unique_skill_vacancy"
            ),
        ),
    ]
