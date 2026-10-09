from django.contrib import admin
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Shipment, TrackingEvent

class TrackingEventInline(admin.TabularInline):
    model = TrackingEvent
    extra = 1

@admin.action(description="Print Shipping Label for Selected Items")
def print_shipping_label(modeladmin, request, queryset):
    # Renders a printable shipping label page for admin
    html = render_to_string('logistics/admin_label.html', {'shipments': queryset})
    return HttpResponse(html)

@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('tracking_number', 'sender_name', 'receiver_name', 'origin', 'destination', 'status', 'created_at')
    search_fields = ('tracking_number', 'sender_name', 'receiver_name')
    list_filter = ('status',)
    inlines = [TrackingEventInline]
    actions = [print_shipping_label]