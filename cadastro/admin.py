from django.contrib import admin

from .models import Estado, Cidade, Pais

# Register your models here.

admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Pais)


