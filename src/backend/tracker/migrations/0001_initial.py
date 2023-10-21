# Generated by Django 4.2.6 on 2023-10-21 09:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название навыка', max_length=50, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Навык',
                'verbose_name_plural': 'Навыки',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название вакансии', max_length=50, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='VacancySkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.PositiveSmallIntegerField(default=1, help_text='Важность навыка', validators=[django.core.validators.MinValueValidator(1, 'Как минимум 1'), django.core.validators.MaxValueValidator(5, 'Как максимум 5')], verbose_name='Вес')),
                ('skill', models.ForeignKey(help_text='Связанный навык', on_delete=django.db.models.deletion.CASCADE, related_name='vacancy', to='tracker.skill', verbose_name='Навыки')),
                ('vacancy', models.ForeignKey(help_text='В каких вакансиях', on_delete=django.db.models.deletion.CASCADE, related_name='skill', to='tracker.vacancy', verbose_name='Вакансии')),
            ],
            options={
                'verbose_name': 'Навык',
                'verbose_name_plural': 'Навыки',
            },
        ),
        migrations.AddField(
            model_name='vacancy',
            name='skills',
            field=models.ManyToManyField(help_text='Навыки', related_name='vacancies', through='tracker.VacancySkill', to='tracker.skill', verbose_name='Навыки'),
        ),
        migrations.AddConstraint(
            model_name='vacancyskill',
            constraint=models.UniqueConstraint(fields=('vacancy', 'skill'), name='unique_vacancy_skill'),
        ),
    ]
