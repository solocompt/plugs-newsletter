"""
Newsletter views
"""
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes

from plugs_newsletter import models
from plugs_newsletter import serializers
from plugs_newsletter import signals

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def subscribe(request):
    """
    Subscribe newsletter
    """
    serializer = serializers.SubscriptionSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    subscription = serializer.save()
    subscription.send_subscribed_email()
    signals.email_added_to_newsletter.send(sender=subscription)
    data = {"message": _("Subscribed successfuly.")}
    return Response(data=data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def unsubscribe(request):
    """
    Unsubscribe from the newsletter
    """
    kwargs = {'email': request.data.get('email')}
    subscription = get_object_or_404(models.Subscription, **kwargs)
    signals.email_removed_from_newsletter.send(sender=subscription)
    subscription.delete()
    subscription.send_unsubscribed_email()
    data = {"message": _("Unsubscribed successfuly from the newsletter")}
    return Response(data=data, status=status.HTTP_200_OK)    
