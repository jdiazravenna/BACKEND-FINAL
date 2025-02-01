"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv
import os
load_dotenv()
print("ENGINE:", os.getenv("ENGINE"))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+67_t3f%x62bg$s!(bmq@wiqq+xnpm$h8!1q2()gxl6&m(zxcs'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*'] # PERMITIMOS SOLICITUDES DE TODAS LAS RUTAS


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'users',
    'products',
    'drf_yasg',
    "corsheaders",
    "orders",
]


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),  # Token dura 60 minutos
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),  # Refresh Token dura 7 días
    "ROTATE_REFRESH_TOKENS": True,  # Genera un nuevo refresh token al usarlo
    "BLACKLIST_AFTER_ROTATION": True,  # Invalida el refresh token después de usarlo
    "AUTH_HEADER_TYPES": ("Bearer",),  # Tipo de autenticación con "Bearer"
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]


CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173", # Ajusta esto si tu frontend está en otro puerto
]

CORS_ALLOW_CREDENTIALS = True


ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecommerce.wsgi.application'
AUTH_USER_MODEL = 'users.CustomUser'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# postgresql://ecommerce_db_j9t1_user:
# PeLcc7uTgqJEHVjoBckLwoadfr2wI6V7
# @dpg-cuelu62j1k6c73ckkn70-a.virginia-postgres.render.com/
# ecommerce_db_j9t1

DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.postgresql",
        'NAME': "ecommerce_db_j9t1",
        'USER': "ecommerce_db_j9t1_user",  # Usuario configurado
        'PASSWORD': "PeLcc7uTgqJEHVjoBckLwoadfr2wI6V7",  # Contraseña configurada al instalar PostgreSQL
        'HOST': "dpg-cuelu62j1k6c73ckkn70-a.virginia-postgres.render.com"  # Servidor local
        # 'PORT': '5432',       # Puerto predeterminado
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]




# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_ROOT = BASE_DIR/'static'
