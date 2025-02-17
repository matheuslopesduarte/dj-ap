from django.contrib import admin

from hospital.models import Paciente, Medico, Consulta

# Register your models here.

admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Consulta)