"""
Testing Views
"""

from rest_framework.test import APIRequestFactory

from plugs_core.testcases import PlugsAPITestCase
from plugs_newsletter import views

factory = APIRequestFactory()

class TestsViews(PlugsAPITestCase):
    """
    Testing Views
    """
    
    def test_subscribe_using_valid_email(self):
        """
        Ensures guest can subscribe with valid email
        """
        request = factory.post('', data={'email': 'janedoe@example.com'})
        response = views.subscribe(request)
        self.assert201(response)

        
    def test_subscribe_using_valid_email(self):
        """
        Ensures guest can subscribe with valid email
        """
        request = factory.post('', data={'email': 'janedoe@example.com'})
        response = views.subscribe(request)
        self.assert201(response)

    
    def test_cannot_subscribe_twice_with_same_email(self):
        """
        Ensures cannot subscribe twice with same email
        """
        request = factory.post('', data={'email': 'janedoe@example.com'})
        response = views.subscribe(request)
        self.assert201(response)

        request = factory.post('', data={'email': 'janedoe@example.com'})
        response = views.subscribe(request)
        self.assert400(response)


    def test_can_unsubscribe(self):
        """
        Ensures guest can unsubscribe
        """
        request = factory.post('', data={'email': 'janedoe@example.com'})
        response = views.subscribe(request)
        self.assert201(response)

        request = factory.post('', data={'email': 'janedoe@example.com'})
        response = views.unsubscribe(request)
        self.assert200(response)

    def test_cannot_unsubscribe(self):
        """
        Ensures guest cannot unsubscribe
        """
        request = factory.post('', data={'email': 'janedoe@example.com'})
        response = views.unsubscribe(request)
        self.assert404(response)
