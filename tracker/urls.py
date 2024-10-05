from . import views
from django.urls import path

urlpatterns = [
    path('overview/', views.overview, name='overview'),
    path('income/', views.income, name='income'),
    path('expense/', views.income, name='expense'),
]