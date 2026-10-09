from django.contrib import admin
from django.urls import path
from logistics import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('track/<str:tracking_number>/', views.track_shipment_view, name='track_shipment'),
    path('services/', views.services_view, name='services'),
]