"""
Plugs Newsletter Models
"""

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

from plugs_core import mixins
from plugs_mail.utils import to_email 

from plugs_newsletter import emails

class Subscription(mixins.Timestampable, models.Model):
    """
    Newsletter subscription
    """
    error_msgs = {'unique': _('This email is already registered.')}
    email = models.EmailField(unique=True, error_messages=error_msgs)
    first_name = models.CharField(max_length=35, null=True)
    last_name = models.CharField(max_length=35, null=True)

    def __str__(self):
        return self.email

    def send_subscribed_email(self):
        """
        Send newsletter subscribed successfuly to subscriber
        """
        to_email(emails.NewsletterSubscribed, self.email)

    def send_unsubscribed_email(self):
        """
        Send newsletter unsubscribed successfuly to subscriber
        """
        to_email(emails.NewsletterUnsubscribed, self.email)

    # pylint: disable=R0903
    class Meta:
        """
        Providing verbose names is recommended if
        we want to use i18n in admin site
        """
        verbose_name = _('subscription')
        verbose_name_plural = _('subscriptions')
