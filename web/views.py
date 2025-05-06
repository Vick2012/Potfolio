from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contacto

def home(request):
    return render(request, 'web/index.html')

def contacto_page(request):
    return render(request, 'web/contacto.html')

def enviar_contacto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        email = request.POST['email']
        mensaje = request.POST['mensaje']
        Contacto.objects.create(nombre=nombre, email=email, mensaje=mensaje)
        messages.success(request, '¡Mensaje enviado con éxito!')
        return redirect('/')
    return redirect('/')

