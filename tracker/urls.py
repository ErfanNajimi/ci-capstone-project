from . import views
from django.urls import path

urlpatterns = [
    path('', views.tracker, name='tracker'),
    path('tracker/income_delete/<int:income_id>',
         views.income_delete, name='income_delete'),
]