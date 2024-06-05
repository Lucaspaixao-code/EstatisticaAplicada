from django.urls import path
from django.views.generic.base import RedirectView
from app_CalculadoraFinanciamento import views

urlpatterns = [
    path('', RedirectView.as_view(url='home', permanent=True)),
    path('home/', views.home, name='home'),
    path('relatorio/', views.relatorio, name='relatorio')
]
