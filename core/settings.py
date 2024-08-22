from pathlib import Path
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.templatetags.static import static
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4r7lr+_@g0q-@u58-0&bf4i6foga@8jx4!h4kdzyhkvk7n8qd1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


UNFOLD = {
    "SITE_TITLE": "Portifolio ibanez.dev.br",
    "SITE_HEADER": "Ibanez.",
    "SITE_URL": "/",
    "SITE_SYMBOL": "widgets",
    "THEME": "dark",

    "COLORS": {
    "primary": {
    "50": "236 253 245",   # Esmeralda muito claro
    "100": "209 250 229",  # Esmeralda claro
    "200": "167 243 208",  # Esmeralda claro médio
    "300": "110 231 183",  # Esmeralda médio
    "400": "52 211 153",   # Esmeralda intenso
    "500": "16 185 129",   # Esmeralda padrão
    "600": "5 150 105",    # Esmeralda escuro
    "700": "4 120 87",     # Esmeralda profundo
    "800": "6 95 70",      # Esmeralda muito escuro
    "900": "6 78 59",      # Esmeralda quase preto
    "950": "2 44 34"       # Esmeralda mais escuro
}

    },

     "SIDEBAR": {
        "show_all_applications": True,
        "navigation": [
            {
                
                "items": [{
                    "title": _("Administradores"),
                    "icon": "admin_panel_settings",
                    "link": reverse_lazy("admin:auth_user_changelist"),
                    "permission": lambda request: request.user.is_superuser,
                    
                },


                {
                    "title": _("Hero Section"),
                    "icon": "home",
                    "link": reverse_lazy("admin:api_pageinfo_changelist"),
                    "permission": lambda request: request.user.is_superuser,
                    
                },

                {
                    "title": _("Projetos"),
                    "icon": "code",
                    "link": reverse_lazy("admin:api_project_changelist"),
                    "permission": lambda request: request.user.is_superuser,
                    
                },

                {
                    "title": _("Tecnologias"),
                    "icon": "editor_choice",
                    "link": reverse_lazy("admin:api_technology_changelist"),
                    "permission": lambda request: request.user.is_superuser,
                    
                },

                {
                    "title": _("Destaques"),
                    "icon": "trending_up",
                    "link": reverse_lazy("admin:api_highlightprojects_changelist"),
                    "permission": lambda request: request.user.is_superuser,
                    
                },

                {
                    "title": _("Conhecimentos"),
                    "icon": "school",
                    "link": reverse_lazy("admin:api_knowtechs_changelist"),
                    "permission": lambda request: request.user.is_superuser,
                    
                },

                {
                    "title": _("Experiência Profissional"),
                    "icon": "work_history",
                    "link": reverse_lazy("admin:api_workexperience_changelist"),
                    "permission": lambda request: request.user.is_superuser,
                    
                },

                {
                    "title": _("Contato"),
                    "icon": "support_agent",
                    "link": reverse_lazy("admin:api_social_changelist"),
                    "permission": lambda request: request.user.is_superuser,
                    
                },

                
                ]
            }
        ]
    },

}


# Application definition

INSTALLED_APPS = [
    "unfold",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'graphene_django',
    'api',
    "django_ckeditor_5",
    
    
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

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True




STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


GRAPHENE = {
    "SCHEMA": "api.schema.schema"
}


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CSRF_TRUSTED_ORIGINS = [
    'http://localhost',
]




customColorPalette = [
        {
            'color': 'hsl(140, 60%, 50%)',

            'label': 'Emerald'
        },

        {
            'color': 'hsl(4, 90%, 58%)',
            'label': 'Red'
        },

        {
            'color': 'hsl(340, 82%, 52%)',
            'label': 'Pink'
        },
        {
            'color': 'hsl(291, 64%, 42%)',
            'label': 'Purple'
        },
        {
            'color': 'hsl(262, 52%, 47%)',
            'label': 'Deep Purple'
        },
        {
            'color': 'hsl(231, 48%, 48%)',
            'label': 'Indigo'
        },
        {
            'color': 'hsl(207, 90%, 54%)',
            'label': 'Blue'
        },
    ]




CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': ['heading', '|', 'bold', 'italic', 'link', 'fontColor', 'FontBackgroundColor',],
        
        

    },
    'extends': {
        'blockToolbar': [
            'paragraph', 'heading1', 'heading2', 'heading3',
            '|',
            'bulletedList', 'numberedList',
            '|',
            'blockQuote',
        ],
        'toolbar': ['heading', '|', 'outdent', 'indent', '|', 'bold', 'italic', 'link', 'underline', 'strikethrough',
        'code','subscript', 'superscript', 'highlight', '|', 'codeBlock', 'sourceEditing', 'insertImage',
                    'bulletedList', 'numberedList', 'todoList', '|',  'blockQuote', 'imageUpload', '|',
                    'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', 'mediaEmbed', 'removeFormat',
                    'insertTable',],
        'image': {
            'toolbar': ['imageTextAlternative', '|', 'imageStyle:alignLeft',
                        'imageStyle:alignRight', 'imageStyle:alignCenter', 'imageStyle:side',  '|'],
            'styles': [
                'full',
                'side',
                'alignLeft',
                'alignRight',
                'alignCenter',
            ]

        },
        'table': {
            'contentToolbar': [ 'tableColumn', 'tableRow', 'mergeTableCells',
            'tableProperties', 'tableCellProperties' ],
            'tableProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            },
            'tableCellProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            }
        },
        'heading' : {
            'options': [
                { 'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph' },
                { 'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1' },
                { 'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2' },
                { 'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3' }
            ]
        }
    },
    'list': {
        'properties': {
            'styles': 'true',
            'startIndex': 'true',
            'reversed': 'true',
        }
    }
}




LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

LOGOUT_REDIRECT_URL = '/admin/'