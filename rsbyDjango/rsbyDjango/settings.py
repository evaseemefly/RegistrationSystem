"""
Django settings for rsbyDjango project.

Generated by 'django-admin startproject' using Django 1.11.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os,sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0,BASE_DIR)
#添加apps的目录地址
sys.path.insert(0,os.path.join(BASE_DIR,'apps'))
# 将根目录下的extra_sourcecode加入到系统路径中
sys.path.insert(0,os.path.join(BASE_DIR,'extra_sourcecode'))
BASE_TEMPLATE_DIRS = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))#获取当前脚本的父目录

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'seuko=23hh1b(02dj1b#qi^)=wv8q#18a*y8_xthu-u_+)gze$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['localhost:8000','localhost:8020','127.0.0.1','127.0.0.1:8000']
ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rsdb',
    'duty',
    # 以下三个为xadmin使用的app
    'xadmin',
    'crispy_forms',

    'rest_framework',
    'corsheaders'
    # 'reversion',

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'rsbyDjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'rsbyDjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME':'registrationsystem',

        # 单位台式机
        # 'USER':'admin',
        # 'PASSWORD':'admin123',

        # 540配置
        'USER':'root',
        'PASSWORD':'123456',
        'HOST':'127.0.0.1',
        # 'OPTIONS':{'init_command':'SET storage_engine=INNODB;'}
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CORS_ALLOW_CREDENTIALS = True
# 处理跨域访问的问题
CORS_ORIGIN_ALLOW_ALL = True

# 默认值是全部
CORS_ORIGIN_WHITELIST = (
    # 'localhost:8000',
    # 'localhost:8020',
    # '127.0.0.1',
    # '127.0.0.1:8020',
    # '127.0.0.1:8000'
)

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR,'static')

STATICFILES_DIRS = [
    # os.path.join(STATIC_ROOT, "static").replace('\\', '/'),
    ('css', os.path.join(STATIC_ROOT, 'css').replace('\\', '/')),
    ('js', os.path.join(STATIC_ROOT, 'js').replace('\\', '/')),
    ('fonts', os.path.join(STATIC_ROOT, 'fonts').replace('\\', '/')),
    ('img', os.path.join(STATIC_ROOT, 'img').replace('\\', '/')),
    # ('images', os.path.join(STATIC_ROOT, 'images').replace('\\', '/')),
    # ('upload', os.path.join(STATIC_ROOT, 'upload').replace('\\', '/')),
]

TEMPLATE_DIRS = (
    os.path.join(BASE_TEMPLATE_DIRS,  'templates'),
)

REDIS_IP='127.0.0.1'
REDIS_PORT=6379
#redis过期时间
REDIS_EX=85400

NAME_DaySavedInRedis='dailydata'