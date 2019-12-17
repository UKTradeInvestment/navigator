from .base import *

DEBUG = False

ALLOWED_HOSTS = ['selling-online-overseas.export.staging.uktrade.io',
                 'selling-online-overseas.export.great.staging.uktrade.io',
                 'selling-online-overseas.export.great.uat.uktrade.io',
                 'selling-online-overseas.export.great.dev.uktrade.io',
                 'great.dev.uktrade.io',
                 'great.staging.uktrade.io',
                 'great.uat.uktrade.io',
                 'great.dev.uktrade.digital',
                 'great.staging.uktrade.digital',
                 'great.uat.uktrade.digital',
                 'navigator-dev.london.cloudapps.digital',
                 'navigator-uat.london.cloudapps.digital',
                 'navigator-staging.london.cloudapps.digital']

INSTALLED_APPS += [
    'raven.contrib.django.raven_compat'
]

RESTRICT_IPS = True
ALLOW_AUTHENTICATED = True
ALLOW_ADMIN = True

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# Activity Stream API
ACTIVITY_STREAM_ACCESS_KEY_ID = env.str('ACTIVITY_STREAM_ACCESS_KEY_ID')
ACTIVITY_STREAM_SECRET_ACCESS_KEY = env.str('ACTIVITY_STREAM_SECRET_ACCESS_KEY')
