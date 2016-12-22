"""
Newsletter APP Settings
"""

from django.conf import settings

PROJECT_SETTINGS = getattr(settings, 'PLUGS_NEWSLETTER', {})

DEFAULTS = {
    'NEWSLETTER_ENDPOINT': 'newsletter',
}

if not PROJECT_SETTINGS.get('NEWSLETTER_ENDPOINT'):
    PROJECT_SETTINGS['NEWSLETTER_ENDPOINT'] = DEFAULTS['NEWSLETTER_ENDPOINT']

plugs_newsletter_settings = PROJECT_SETTINGS
