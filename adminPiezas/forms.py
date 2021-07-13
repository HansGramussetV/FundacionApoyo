from django import  forms
from django.db.models.base import Model
from django.forms import ModelForm
from .models import Pieza, Residente

class crearForm(ModelForm):
    class Meta():
        model = Residente
        fields = [
            'nombre', 
            'apellido', 
            'rut', 
            'fechaNacimiento'
        ]
        labels = {
            'nombre' : 'Nombre', 
            'apellido' : 'Apellido',
            'rut' : 'Rut',
            'fechaNacimiento' : 'Fecha de nacimiento' 
        }



class piezaForm(ModelForm):

    class  Meta():
        model = Pieza
        fields = ['residente', 'paramedico']


class verForm(ModelForm):
    class Meta():
        model = Pieza
        fields = ['residente']