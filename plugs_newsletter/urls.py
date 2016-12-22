"""
Newsletter APP urls
"""

from django.conf.urls import url

from plugs_newsletter import views
from plugs_newsletter.settings import plugs_newsletter_settings

endpoint = plugs_newsletter_settings['NEWSLETTER_ENDPOINT']

urlpatterns = [
    url(r'^' + endpoint + r'/subscribe/$', views.subscribe),
    url(r'^' + endpoint + r'/unsubscribe/$', views.unsubscribe)
]
