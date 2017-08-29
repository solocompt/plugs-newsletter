"""
Newsletter Serializers
"""

from rest_framework import serializers

from plugs_newsletter import models

class SubscriptionSerializer(serializers.ModelSerializer):
    """
    Subscription Serializer
    """
    # pylint: disable=R0903
    class Meta:
        """
        Metaclass definition
        """
        model = models.Subscription
        fields = ('id', 'email', 'name', 'created', 'updated')
