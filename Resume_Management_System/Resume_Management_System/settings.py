import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-c9)%4wt#e0fwtjf!juw&z1lz7v7a8i*%h^f$rc@n!9^n5b@t8+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['nikibhole.pythonanywhere.com']

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tinymce',
    'jobportal'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Resume_Management_System.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Resume_Management_System.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'resume_management_system',
        'USER': 'root',
        'PASSWORD': 'Nikitabhole95@',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
    # "/var/www/static/",
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JAZZMIN_SETTINGS = {
    "site_title": "Resume Management Admin",
    "site_header": "Resume Management",
    "site_brand": "RMS Admin",

    # "site_logo": "imgs/talent-search.png",
    #
    # "site_logo_classes": "img-circle",
    # "custom_css": "CSS/j_page.CSS",

    "user_avatar": "profile.image",

    "welcome_sign": "Welcome to the Resume Portal",

    "copyright": "jobhunter Soft Pvt. Ltd",

    "search_model": ["auth.User", "auth.Group"],

    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.User"},
        {"app": "Resume_Management_System"},
    ],

    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],

    "show_sidebar": True,
    "navigation_expanded": True,

    "custom_links": {
        "resume_management_system": [
            {
                "name": "Manage Jobs",
                "url": "job_management",
                "icon": "fas fa-briefcase",
                "permissions": ["resume_management_system.view_job"]
            }
        ]
    },

    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",

        "resume_management_system": "fas fa-id-card",
        "jobportal.user": "fas fa-user-tie",
        "jobportal.job": "fas fa-briefcase",
        "jobportal.application": "fas fa-file-alt",  # Applications
        "jobportal.skill": "fas fa-lightbulb",

        "jobportal.aptitudepaper": "fas fa-book-open",  # 📖 Aptitude Papers
        "jobportal.careertips": "fas fa-lightbulb",  # 💡 Career Tips
        "jobportal.hrquestion": "fas fa-comments",  # 💬 HR Questions
        "jobportal.mocktestschedule": "fas fa-calendar-check",  # 📅 Mock Test Schedules
    },

    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs"
    },
}

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_URL = '/login/'

# TINYMCE_DEFAULT_CONFIG = {
#     'height': 400,
#     'width': 900,
#     'menubar': 'file edit view insert format tools table help',
#     'plugins': 'advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code fullscreen insertdatetime media table paste code help wordcount',
#     'toolbar': 'undo redo | formatselect | bold italic backcolor | \
#                 alignleft aligncenter alignright alignjustify | \
#                 bullist numlist outdent indent | removeformat | code',
# }


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'kartikbhole791@gmail.com'
EMAIL_HOST_PASSWORD = 'ldbb nedi dvea ngiz'

DEFAULT_FROM_EMAIL = 'kartikbhole791@gmail.com'
CONTACT_EMAIL = 'kartikbhole791@gmail.com'
