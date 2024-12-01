from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def index(request):
    return render(request, 'index.html')

def saludar(request, nombre):
    return HttpResponse(f"Bienvenid@ {nombre}")

def alumnos_por_anio(request, year):
    alumnos=["Carlos","Maria","Jose"]
    return HttpResponse(f"Listado de alumnos: {year} \n {alumnos}")