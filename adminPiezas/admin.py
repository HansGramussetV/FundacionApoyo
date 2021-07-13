from django.contrib import admin
from .models import Residente, Pieza, Paramedico


# Register your models here.

admin.site.register(Residente)
admin.site.register(Pieza)
admin.site.register(Paramedico)