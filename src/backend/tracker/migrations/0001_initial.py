# Generated by Django 4.2.6 on 2023-10-21 18:43

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название города', max_length=50, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Mуж.'), ('F', 'Жен.')], help_text='Пол кандидата', max_length=1, verbose_name='Пол')),
                ('telegram', models.CharField(help_text='Телеграм', max_length=50, verbose_name='Телеграм')),
                ('github', models.CharField(help_text='GitHub', max_length=50, verbose_name='GitHub')),
                ('about_me', models.TextField(help_text='О себе', verbose_name='О себе')),
                ('birthday', models.DateField(blank=True, help_text='День рождкния', null=True, verbose_name='День рождения')),
                ('status_type_work', models.PositiveSmallIntegerField(choices=[(0, 'Не известно'), (1, 'Оффис'), (2, 'Гибрид'), (3, 'Удаленка')], default=0, help_text='Какой устраивает тип работы кандидата', verbose_name='Тип работы')),
                ('status_finded', models.PositiveSmallIntegerField(choices=[(0, 'Не известно'), (1, 'В поиске'), (2, 'В отпуске'), (3, 'Найден')], default=0, help_text='Стадия поиска работы кандидата', verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Резюме',
                'verbose_name_plural': 'Резюме',
                'ordering': ['candidate'],
            },
        ),
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
                ('description', models.TextField(blank=True, help_text='Описание вакансии', null=True, verbose_name='Описание')),
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
        migrations.CreateModel(
            name='ResumeSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveSmallIntegerField(default=1, help_text='Уровень навыка', verbose_name='Уровень')),
                ('resume', models.ForeignKey(help_text='В каких резюме', on_delete=django.db.models.deletion.CASCADE, related_name='skill', to='tracker.resume', verbose_name='Резюме')),
                ('skill', models.ForeignKey(help_text='Связанный навык', on_delete=django.db.models.deletion.CASCADE, related_name='resume', to='tracker.skill', verbose_name='Навыки')),
            ],
            options={
                'verbose_name': 'Навык',
                'verbose_name_plural': 'Навыки',
            },
        ),
    ]
