from django.contrib import admin

#AGREGAMOS LA APLICACION DE ENCUESTA PARA VERLA 
#EN EL ADMINISTRADOR
from .models import Question

admin.site.register(Question)
# Register your models here.
