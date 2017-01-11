"""
Plugs Newsletter Signals
"""

from django.dispatch import Signal

# sent when an email was added to the newsletter
email_added_to_newsletter = Signal()

# sent when an email was removed from the newsletter
email_removed_from_newsletter = Signal()
