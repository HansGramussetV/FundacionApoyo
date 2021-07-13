from typing import ValuesView
from django.forms.models import ALL_FIELDS
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Pieza, Residente, Paramedico
from .forms import  piezaForm, crearForm
# Create your views here.

def home(request):
    piezas = Pieza.objects.all()
    datos = {
        'piezas': piezas,
    }
    return render(request, 'adminPiezas/home.html', datos)
    

def editForm(request, nro):
    pieza = Pieza.objects.get(nroPieza = nro)

    datos = {
        'form': piezaForm(instance= pieza)

    }

    if request.method == 'POST':
        formulario_edit = piezaForm(data = request.POST, instance= pieza)
        if formulario_edit.is_valid():
            formulario_edit.save()

            datos['mensaje'] = "Pieza modificada con exito"


    return render(request,'adminPiezas/formPieza.html', datos )

def crear_Form(request):
    if request.method == 'POST':
        form = crearForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = crearForm()

    return render(request, 'adminPiezas/formCrear.html', {'form' :form})

def quitForm(request, nro):
    pieza = Pieza.objects.get(nroPieza = nro)

    datos = {
        

    }

    if request.method == 'POST':
        formulario_edit = piezaForm(data = request.POST, instance= pieza)
        if formulario_edit.is_valid():
            formulario_edit.save()

            datos['mensaje'] = "Pieza Eliminada con éxito"


    return render(request,'adminPiezas/formQuit.html', datos)


def resident_list(request):
    resident = Residente.objects.all()
    contexto = {'residents' : resident}
    return render(request, 'adminPiezas/fichapas.html', contexto)

def para_list(request):
    paramedic = Paramedico.objects.all()
    contexto = {'parameds' : paramedic}
    return render (request, 'adminPiezas/fichapara.html', contexto)

def ficha_med(request):
    fichamed = Residente.objects.all()
    contexto = {'ficha' : fichamed}
    return render(request, 'adminPiezas/fichamed.html', contexto)
