from . import views
from django.urls import path

urlpatterns = [
    path('', views.tracker, name='tracker'),
]