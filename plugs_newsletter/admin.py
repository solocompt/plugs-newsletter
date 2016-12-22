from django.contrib import admin

from plugs_newsletter.models import Subscription

class SubscriptionAdmin(admin.ModelAdmin):
    """
    Subscription Model Admin
    """
    fields = ('email', 'first_name', 'last_name', 'created', 'updated')
    readonly_fields = ('id', 'created', 'updated')
    list_display = ('email', 'first_name', 'last_name')
    search_fields = ('email', 'first_name', 'last_name')

admin.site.register(Subscription, SubscriptionAdmin)
