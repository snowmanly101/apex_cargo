from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Shipment

def home_view(request):
    if request.method == 'POST':
        tracking_code = request.POST.get('tracking_number', '').strip()
        if tracking_code:
            return redirect('track_shipment', tracking_number=tracking_code)
        messages.error(request, "Please enter a valid tracking number.")
    return render(request, 'logistics/index.html')

def track_shipment_view(request, tracking_number):
    shipment = Shipment.objects.filter(tracking_number__iexact=tracking_number).first()
    context = {
        'shipment': shipment,
        'searched_code': tracking_number
    }
    return render(request, 'logistics/track.html', context)

def services_view(request):
    return render(request, 'logistics/services.html')