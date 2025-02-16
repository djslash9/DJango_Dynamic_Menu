from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', views.accounts, name='accounts'),
    path('hr/', views.hr, name='hr'),
    path('it/', views.it, name='it'),
    path('marketing/', views.marketing, name='marketing'),
]
