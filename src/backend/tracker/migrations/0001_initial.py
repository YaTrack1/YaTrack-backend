# Generated by Django 4.2.6 on 2023-10-22 05:07

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("vacancy", "0001_initial"),
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Candidate",
            fields=[
                (
                    "user_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "last_visit",
                    models.DateTimeField(
                        auto_now_add=True,
                        verbose_name="Последнее время онлайна",
                    ),
                ),
                ("birthday", models.DateField(verbose_name="День рождения")),
                ("date_create", models.DateTimeField()),
            ],
            options={
                "verbose_name": "Кандидат",
                "verbose_name_plural": "Кандидаты",
                "ordering": ("username",),
                "default_related_name": "candidates",
            },
            bases=("user.user",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="City",
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
                        help_text="Название города",
                        max_length=50,
                        unique=True,
                        verbose_name="Название",
                    ),
                ),
            ],
            options={
                "verbose_name": "Город",
                "verbose_name_plural": "Города",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Employer",
            fields=[
                (
                    "user_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("date_create", models.DateTimeField()),
            ],
            options={
                "verbose_name": "Наниматель",
                "verbose_name_plural": "Наниматели",
                "default_related_name": "employers",
            },
            bases=("user.user",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
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
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Mуж."), ("F", "Жен.")],
                        help_text="Пол кандидата",
                        max_length=1,
                        verbose_name="Пол",
                    ),
                ),
                (
                    "telegram",
                    models.CharField(
                        help_text="Телеграм",
                        max_length=50,
                        verbose_name="Телеграм",
                    ),
                ),
                (
                    "github",
                    models.CharField(
                        help_text="GitHub",
                        max_length=50,
                        verbose_name="GitHub",
                    ),
                ),
                (
                    "about_me",
                    models.TextField(
                        help_text="О себе", verbose_name="О себе"
                    ),
                ),
                (
                    "birthday",
                    models.DateField(
                        blank=True,
                        help_text="День рождкния",
                        null=True,
                        verbose_name="День рождения",
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
                        help_text="Какой устраивает тип работы кандидата",
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
                        help_text="Стадия поиска работы кандидата",
                        verbose_name="Статус",
                    ),
                ),
                (
                    "candidate",
                    models.ForeignKey(
                        help_text="Кандидат",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="resume",
                        to="tracker.candidate",
                        verbose_name="Кандидат",
                    ),
                ),
                (
                    "city",
                    models.ForeignKey(
                        help_text="Город кондидата",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="candidate",
                        to="tracker.city",
                        verbose_name="Город",
                    ),
                ),
            ],
            options={
                "verbose_name": "Резюме",
                "verbose_name_plural": "Резюме",
                "ordering": ["candidate"],
            },
        ),
        migrations.CreateModel(
            name="ResumeSkill",
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
                    "level",
                    models.PositiveSmallIntegerField(
                        default=1,
                        help_text="Уровень навыка",
                        verbose_name="Уровень",
                    ),
                ),
                (
                    "resume",
                    models.ForeignKey(
                        help_text="В каких резюме",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="skill",
                        to="tracker.resume",
                        verbose_name="Резюме",
                    ),
                ),
                (
                    "skill",
                    models.ForeignKey(
                        help_text="Связанный навык",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="resume",
                        to="vacancy.skill",
                        verbose_name="Навыки",
                    ),
                ),
            ],
            options={
                "verbose_name": "Навык",
                "verbose_name_plural": "Навыки",
            },
        ),
        migrations.AddField(
            model_name="resume",
            name="skills",
            field=models.ManyToManyField(
                help_text="Навыки",
                related_name="resumes",
                through="tracker.ResumeSkill",
                to="vacancy.skill",
                verbose_name="Навыки",
            ),
        ),
        migrations.AddConstraint(
            model_name="resumeskill",
            constraint=models.UniqueConstraint(
                fields=("resume", "skill"), name="unique_resume_skill"
            ),
        ),
    ]
