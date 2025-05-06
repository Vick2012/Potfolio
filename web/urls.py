from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('enviar-contacto/', views.enviar_contacto, name='enviar_contacto'),
]
