from django.urls import path
from app_CalculadoraFinanciamento import views

urlpatterns = [
    path('', views.home, name='home'),
    path('veiculo/', views.veiculo, name='veiculo')
]
