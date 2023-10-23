# Generated by Django 4.2.6 on 2023-10-23 04:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Resume",
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
                ("title", models.CharField()),
                (
                    "photo",
                    models.ImageField(upload_to="photo/", verbose_name="Фото"),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Муж."), ("F", "Жен.")],
                        max_length=1,
                        verbose_name="Пол",
                    ),
                ),
                (
                    "telegram",
                    models.CharField(max_length=50, verbose_name="Телеграм"),
                ),
                (
                    "github",
                    models.CharField(max_length=50, verbose_name="GitHub"),
                ),
                ("about_me", models.TextField(verbose_name="О себе")),
                (
                    "birthday",
                    models.DateField(
                        blank=True, null=True, verbose_name="День рождения"
                    ),
                ),
                (
                    "status_type_work",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (0, "Не известно"),
                            (1, "Оффис"),
                            (2, "Гибрид"),
                            (3, "Удаленка"),
                        ],
                        default=0,
                        verbose_name="Тип работы",
                    ),
                ),
                (
                    "status_finded",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (0, "Не известно"),
                            (1, "В поиске"),
                            (2, "В отпуске"),
                            (3, "Найден"),
                        ],
                        default=0,
                        verbose_name="Статус",
                    ),
                ),
                (
                    "candidate",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="resume",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Кандидат",
                    ),
                ),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="candidate",
                        to="core.city",
                        verbose_name="Город",
                    ),
                ),
            ],
            options={
                "verbose_name": "Резюме",
                "verbose_name_plural": "Резюме",
                "ordering": ["candidate"],
                "default_related_name": "resumes",
            },
        ),
        migrations.CreateModel(
            name="SkillInResume",
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
                    "resume",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="skill_list",
                        to="resume.resume",
                        verbose_name="Резюме",
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
            ],
            options={
                "verbose_name": "Скилл в резюме",
                "verbose_name_plural": "Скиллы в резюме",
                "ordering": ("resume",),
            },
        ),
        migrations.AddConstraint(
            model_name="skillinresume",
            constraint=models.UniqueConstraint(
                fields=("skill", "resume"), name="unique_skill_resume"
            ),
        ),
    ]
