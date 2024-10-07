from . import views
from django.urls import path

urlpatterns = [
    path('income/', views.income, name='income'),
    path('expense/', views.expense, name='expense'),
    path('overview/', views.overview, name='overview'),
]