# Generated by Django 4.2.6 on 2023-10-26 01:33

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="City",
            fields=[
                (
                    "name",
                    models.CharField(
                        max_length=50,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="Название",
                    ),
                ),
            ],
            options={
                "verbose_name": "Город",
                "verbose_name_plural": "Города",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Skill",
            fields=[
                (
                    "name",
                    models.CharField(
                        max_length=50,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="Название",
                    ),
                ),
            ],
            options={
                "verbose_name": "Навык",
                "verbose_name_plural": "Навыки",
                "ordering": ("name",),
            },
        ),
    ]
