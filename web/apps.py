from django.apps import AppConfig
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]



class WebConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'web'
