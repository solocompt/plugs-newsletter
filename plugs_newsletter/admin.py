from django.contrib import admin

from plugs_newsletter.models import Subscription

class SubscriptionAdmin(admin.ModelAdmin):
    """
    Subscription Model Admin
    """
    fields = ('email', 'name', 'created', 'updated')
    readonly_fields = ('id', 'created', 'updated')
    list_display = ('email', 'name')
    search_fields = ('email', 'name')

admin.site.register(Subscription, SubscriptionAdmin)
