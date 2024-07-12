from pathlib import Path
import os
import datetime

BASE_DIR = Path(__file__).resolve().parent.parent.parent

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "user",
    "interview",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


SECRET_KEY = "YOUR_SECRET_KEY"

DEBUG = True

ALLOWED_HOSTS = ["*"]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "csweb.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "static")],
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


WSGI_APPLICATION = "csweb.wsgi.application"
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": datetime.timedelta(minutes=120),
    "REFRESH_TOKEN_LIFETIME": datetime.timedelta(days=30),
    "AUTH_HEADER_TYPES": ("Bearer",),
}

LANGUAGE_CODE = "zh-hans"

TIME_ZONE = "Asia/Shanghai"

USE_I18N = True

USE_TZ = True


STATIC_URL = "/static/"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATIC_ROOT = os.path.join(BASE_DIR, "root_static")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
# 根据路由，判断该路由是否需要验证，如果验证内容不写方法，则全部需要验证，否则写了哪个，哪个需要验证。未提供token，则为匿名用户
AUTHENTICETORS_URL = [
    ("^/interview/question/*", "post",),
    ("^/interview/*", "post",),
    ("^/interview/favorite/*", ),
]
# 根据路由，判断该路由是否需要权限，如果权限不写方法，则全部需要验证，否则写了哪个，哪个需要权限。具体权限是最后一位。以二进制形式,如果不写，默认为0，即不需要权限
# 此路由需要登录，并且提供token, 否则直接拒绝
PERMISSION_URL = []