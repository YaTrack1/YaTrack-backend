# Generated by Django 4.2.6 on 2023-10-29 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("user", "0001_initial"),
        ("core", "0001_initial"),
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
                (
                    "position",
                    models.CharField(max_length=150, verbose_name="Должность"),
                ),
                (
                    "specialty",
                    models.CharField(
                        max_length=150, verbose_name="Специализация"
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Описание"
                    ),
                ),
                (
                    "duties",
                    models.CharField(
                        max_length=150, verbose_name="Обязанности"
                    ),
                ),
                (
                    "conditions",
                    models.CharField(max_length=150, verbose_name="Условия"),
                ),
                (
                    "stages",
                    models.CharField(
                        max_length=150, verbose_name="Этапы отбора"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user.user",
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
                    "importance",
                    models.PositiveSmallIntegerField(
                        default=0, verbose_name="Важность навыка"
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
