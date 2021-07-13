from django.urls import  path
from .views import home, editForm, crear_Form, quitForm, resident_list, para_list, ficha_med

urlpatterns = [
    path('', home, name='home'),
    path('edit-pieza/<nro>', editForm, name='edit-pieza' ),
    path('crear/nuevo', crear_Form, name='crear'),
    path('quit-pieza/<nro>', quitForm, name='quit-pieza'),
    path('ver/residente', resident_list, name='ver'),
    path('ver/paramedico', para_list, name='para'),
    path('ver/fichamedica', ficha_med, name='ficha')
]