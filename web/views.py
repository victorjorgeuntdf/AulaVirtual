from django.shortcuts import render
from django.http import HttpResponse 
from django.shortcuts import redirect 
from django.contrib import messages
from .forms import *

import datetime

# Create your views here.

def index(request):
    # Accedo a la BBDD a traves de los modelos
    context = {
       'nombre': 'Maria',
        'fecha_hora':datetime.datetime.now()
    }
    return render(request, 'web/index.html', context)

def saludar(request, nombre):
    print(request.method)
    return HttpResponse(f"Bienvenid@ {nombre}")

def alumnos_por_anio(request, year):
    alumnos=["Carlos","Maria","Jose"]
    return HttpResponse(f"Listado de alumnos: {year} \n {alumnos}")

def listado_alumnos(request):
    # Accedo a la BBDD a traves de los modelos
    context = {
       'alumnos': [
           'Carlos Lopez',
           'Maria del Cerro',
           'Gaston Perez'
       ],
       'cuota_al_dia': True
    }
    """ context = {
       'alumnos': [
           
       ]
    } """
    return render(request, 'web/listado_alumnos.html', context)

def alta_alumno(request):
    contexto = {}
    if request.method == "GET":
        contexto['alta_alumno_form']= AltaAlumnoForm()
    else: #Asumo que es un POST
        form = AltaAlumnoForm(request.POST)
        contexto['alta_alumno_form'] = form
        
        if form.is_valid():
            messages.success(request, 'El alumno fue dado de alta con exito')

            return redirect('index')

    return render(request, 'web/alta_alumno.html', contexto)