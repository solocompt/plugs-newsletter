"""
Plugs Newsletter Emails
"""

from plugs_mail.mail import PlugsMail

class NewsletterSubscribed(PlugsMail):
    """
    Email sent to subscriber after newsletter subscription
    """
    template = 'NEWSLETTER_SUBSCRIBED'
    description = 'Email sent to subscriber after newsletter subscription'

class NewsletterUnsubscribed(PlugsMail):
    """
    Email sent to subscriber after newsletter unsubscription
    """
    template = 'NEWSLETTER_UNSUBSCRIBED'
    description = 'Email sent to subscriber after newsletter unsubscription'
