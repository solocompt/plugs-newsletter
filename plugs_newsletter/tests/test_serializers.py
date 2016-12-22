"""
Tests Serializers
"""

from django.test import TestCase

from plugs_newsletter import serializers


class TestSerializers(TestCase):
    """
    Tests Serializers
    """

    def test_email_is_required_to_subscribe(self):
        """
        Ensures email is required in subscription serializer
        """
        serializer = serializers.SubscriptionSerializer(data={})
        self.assertFalse(serializer.is_valid())
        self.assertIn('email', serializer.errors.keys())

    def test_subscription_serializer(self):
        """
        Ensures subscription serializer
        """
        data = {'email': 'janedoe@example.com', 'first_name': 'Jane', 'last_name': 'Doe'}
        serializer = serializers.SubscriptionSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data, data)
        self.assertEqual(serializer.errors, {})
