"""
Plugs Newsletter Emails
"""

from plugs_mail.mail import PlugsMail

class NewsletterSubscribed(PlugsMail):
    """
    Email sent to subscriber after newsletter subscription
    """
    template = 'NEWSLETTER_SUBSCRIBED'
    context = ()
    description = 'Email sent to subscriber after newsletter subscription'
    subject = 'Email adicionado à newsletter'

class NewsletterUnsubscribed(PlugsMail):
    """
    Email sent to subscriber after newsletter unsubscription
    """
    template = 'NEWSLETTER_UNSUBSCRIBED'
    context = ()
    description = 'Email sent to subscriber after newsletter unsubscription'
    subject = 'Email removido da newsletter'
