"""Common settings and globals."""
import ConfigParser

import os
from os.path import abspath, basename, dirname, join, normpath
from sys import path

from oscar.defaults import *


########## PATH CONFIGURATION
# Absolute filesystem path to the Django project directory
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Absolute filesystem path to the top-level project folder
SITE_ROOT = dirname(DJANGO_ROOT)

# Site name
SITE_NAME = basename(DJANGO_ROOT)

# Add our project to our pythonpath; this way, we don't need to type our project
# name in our dotted import paths
path.append(DJANGO_ROOT)
########## END PATH CONFIGURATION


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('Your Name', 'your_email@example.com'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
########## END MANAGER CONFIGURATION


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
########## END DATABASE CONFIGURATION


########## GENERAL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = 'America/New_York'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

LOCALE_PATHS = (
    join(SITE_ROOT, 'conf', 'locale'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

FORMAT_MODULE_PATH = 'formats'
########## END GENERAL CONFIGURATION


########## MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'
########## END MEDIA CONFIGURATION


########## STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = normpath(join(SITE_ROOT, 'assets'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    normpath(join(SITE_ROOT, 'static')),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter']
########## END STATIC FILE CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key should only be used for development and testing.
SECRET_KEY = os.environ.get("ECOMMERCE_SECRET_KEY", "insecure-secret-key")
########## END SECRET CONFIGURATION


########## SITE CONFIGURATION
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []
########## END SITE CONFIGURATION


########## FIXTURE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    normpath(join(SITE_ROOT, 'fixtures')),
)
########## END FIXTURE CONFIGURATION


########## TEMPLATE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'oscar.apps.search.context_processors.search_form',
    'oscar.apps.promotions.context_processors.promotions',
    'oscar.apps.checkout.context_processors.checkout',
    'oscar.apps.customer.notifications.context_processors.notifications',
    'oscar.core.context_processors.metadata',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

from oscar import OSCAR_MAIN_TEMPLATE_DIR
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
TEMPLATE_DIRS = (
    normpath(join(SITE_ROOT, 'templates')),
    OSCAR_MAIN_TEMPLATE_DIR,
)

ALLOWED_INCLUDE_ROOTS = (
    normpath(join(SITE_ROOT, 'templates')),
)

########## END TEMPLATE CONFIGURATION


########## MIDDLEWARE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'waffle.middleware.WaffleMiddleware',
    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)
########## END MIDDLEWARE CONFIGURATION


########## URL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = '%s.urls' % SITE_NAME
########## END URL CONFIGURATION


########## APP CONFIGURATION
DJANGO_APPS = [
    # Default Django apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',

    # Useful template tags
    'django.contrib.humanize',

    # Django REST framework
    'rest_framework',

    # Admin panel and documentation
    'django.contrib.admin',

    # Feature gating
    'waffle',

    # Static file compression
    'compressor',
]

# Apps specific for this project go here.
LOCAL_APPS = [
    'health',
]

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
from oscar import get_core_apps
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + get_core_apps()
########## END APP CONFIGURATION


########## LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
########## END LOGGING CONFIGURATION


########## WSGI CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'wsgi.application'
########## END WSGI CONFIGURATION

########## SEGMENT.IO
# 'None' disables tracking. This will be turned on for test and production.
SEGMENT_KEY = None

# Regular expression used to identify users that should be ignored in reporting.
# This value will be compiled and should be either a string (e.g. when importing with YAML) or
# a Python regex type.
SEGMENT_IGNORE_EMAIL_REGEX = None
########## END SEGMENT.IO

########## FEEDBACK AND SUPPORT -- These values should be overridden for production deployments.
FEEDBACK_EMAIL = 'override.this.email@example.com'
SUPPORT_URL = 'http://example.com/'
PRIVACY_POLICY_URL = 'http://example.com/'
TERMS_OF_SERVICE_URL = 'http://example.com/'
HELP_URL = None
########## END FEEDBACK

########## LANDING PAGE -- URLs should be overridden for production deployments.
SHOW_LANDING_RESEARCH = True
RESEARCH_URL = 'http://example.com/'
OPEN_SOURCE_URL = 'http://example.com/'
########## END FEEDBACK

########## DOCUMENTATION LINKS -- These values should be overridden for production deployments.
DOCUMENTATION_LOAD_ERROR_URL = 'http://example.com/'
# evaluated again at the end of production setting after DOCUMENTATION_LOAD_ERROR_URL has been set
DOCUMENTATION_LOAD_ERROR_MESSAGE = '<a href="{error_documentation_link}" target="_blank">Read more</a>.'.format(error_documentation_link=DOCUMENTATION_LOAD_ERROR_URL)

########## END FEEDBACK

# The application and platform display names to be used in templates, emails, etc.
PLATFORM_NAME = 'Your Platform Name Here'

########## DOCS/HELP CONFIGURATION
DOCS_ROOT = join(dirname(SITE_ROOT), 'docs')

# Load the docs config into memory when the server starts
# with open(join(DOCS_ROOT, "config.ini")) as config_file:
#     DOCS_CONFIG = ConfigParser.ConfigParser()
#     DOCS_CONFIG.readfp(config_file)
########## END DOCS/HELP CONFIGURATION

########## THEME CONFIGURATION
# Path of the SCSS file to use for the site's theme
THEME_SCSS = 'sass/themes/open-edx.scss'
########## END THEME CONFIGURATION


########## OSCAR SETTINGS

# Order processing
# ================

# The initial status for an order, or an order line.
OSCAR_INITIAL_ORDER_STATUS = 'Open'
OSCAR_INITIAL_LINE_STATUS = 'Open'

# This dict defines the new order statuses than an order can move to
OSCAR_ORDER_STATUS_PIPELINE = {
    'Open': ('Being Processed', 'Order Cancelled',),
    'Order Cancelled': (),
    'Being Processed': ('Paid', 'Payment Cancelled',),
    'Payment Cancelled': (),
    'Paid': ('Complete', 'Fulfillment Error',),
    'Fulfillment Error': ('Complete', 'Refunded',),
    'Complete': ('Refunded',),
    'Refunded': (),
}

# This dict defines the line statuses that will be set when an order's status
# is changed
OSCAR_ORDER_STATUS_CASCADE = {
    'Being Processed': 'Being Processed',
    'Paid': 'Paid',
    'Cancelled': 'Cancelled',
    'Complete': 'Fulfilled',
    'Refunded': 'Refunded',
}

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

# TODO: Replace with new Authentication backend
AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

########## END OSCAR SETTINGS