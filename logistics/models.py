import uuid
from django.db import models

class Shipment(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending Pickup'),
        ('IN_TRANSIT', 'In Transit'),
        ('OUT_FOR_DELIVERY', 'Out for Delivery'),
        ('DELIVERED', 'Delivered'),
        ('HELD', 'Customs / Hub Hold'),
    ]

    tracking_number = models.CharField(max_length=20, unique=True, editable=False)
    sender_name = models.CharField(max_length=100)
    receiver_name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    package_description = models.CharField(max_length=255)
    weight_kg = models.DecimalField(max_digits=6, decimal_places=2, default=1.00)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    estimated_delivery = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.tracking_number:
            # Generates a tracking number like APX-89420391
            self.tracking_number = f"APX-{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.tracking_number} - {self.status}"


class TrackingEvent(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, related_name='events')
    timestamp = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=150)
    description = models.CharField(max_length=255)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.shipment.tracking_number} - {self.location}"