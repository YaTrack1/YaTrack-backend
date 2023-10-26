"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path
from datetime import datetime, timedelta

from django.core.management.utils import get_random_secret_key
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", default=get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "yatrack",
    "51.250.74.42",
    "178.178.89.175",
]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "api.apps.ApiConfig",
    "user.apps.UserConfig",
    "tracker.apps.TrackerConfig",
    "vacancy.apps.VacancyConfig",
    "resume.apps.ResumeConfig",
    "core.apps.CoreConfig",
    "rest_framework",  # isort:ignore
    "rest_framework.authtoken",  # isort:ignore
    "djoser",  # isort:ignore
    "django_filters",  # isort:ignore
    "drf_yasg",  # isort:ignore
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "yatrack.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "yatrack.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.getenv(
            "DB_ENGINE", default="django.db.backends.postgresql"
        ),
        "NAME": os.getenv("DB_NAME", default="ytrack"),
        "USER": os.getenv("PG_USER", default="postgres"),
        "PASSWORD": os.getenv("PG_PASSWORD", default="postgres"),
        "HOST": os.getenv("DB_HOST", default="localhost"),
        "PORT": os.getenv("DB_PORT", default="5432"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "ru-ru"
TIME_ZONE = "Europe/Moscow"

USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_FILTER_BACKENDS": (
        "django_filters.rest_framework.DjangoFilterBackend",
    ),
}

DJOSER = {
    "LOGIN_FIELD": "email",
    # "SEND_ACTIVATION_EMAIL": False,
    # "HIDE_USERS": False,
    # "PERMISSIONS": {
    #     "user": ["djoser.permissions.CurrentUserOrAdminOrReadOnly"],
    #     "user_list": ["rest_framework.permissions.AllowAny"],
    # },
    # "SERIALIZERS": {
    #     # "user": "api.serializers.UserSerializer",
    #     # "current_user": "api.serializers.UserSerializer",
    #     "user_create": "djoser.serializers.UserCreateSerializer",
    # },
}
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "AUTH_HEADER_TYPES": ("Bearer",),
}

AUTH_USER_MODEL = "user.User"


# Константы----------------------------
# -------------------------------------

# Модели
ZERO = 0
MAX_LENGTH = 150

DATETIME_NOW = datetime.now()

GENDER_FLAG = [("M", "Муж."), ("F", "Жен.")]
TYPE_WORK = [(0, "Не известно"), (1, "Оффис"), (2, "Гибрид"), (3, "Удаленка")]
STATUS_FIDED = [
    (0, "Не известно"),
    (1, "В поиске"),
    (2, "В отпуске"),
    (3, "Найден"),
]

# Юзер-админ
MAIL_LENGTH = 255
MAIL_VALID = r"[^@]+@[^@]+\.[^@]+"
MAIL_ERROR = "{} недопустимый формат эл. почты."

USER_VALID = "Нельзя использовать имя: {}!"
CHAR_VALID = r"^[а-яА-ЯёЁa-zA-Z0-9]+$"
CHAR_VALID_USER = r"^[a-zA-Z0-9]+$"

LENGTH_HELP = f"Максимум {MAX_LENGTH} символов."

# Логгер
LOG_FORMAT = "%(asctime)s :: %(name)s:%(lineno)s - %(levelname)s - %(message)s"
LOG_FILE = os.path.join(BASE_DIR / "api/logs/file.log")
LOG_DIR = os.path.join(BASE_DIR / "api/logs")
LOG_MESSAGE = "Custom log"
LOG_PASS_FILTER = "password"

# Парсер
HELP_TEXT_PARSER = "Загрузка данных из {} файла."
DELETE_TEXT_PARSER = "Удаление данных {} файла."

DATA_DIR = "data/{}"
DATA_DELETE = "Данные {} удалены."
DATA_UPLOADED = "Данные {} уже загружены."
DATA_LOAD_IN_FILE = "Загрузка данных из {} завершена."

OPTIONS_DELETE = "delete"
