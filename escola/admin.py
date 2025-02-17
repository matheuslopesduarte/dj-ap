from django.contrib import admin

from escola.models import Aluno, Professor, Turma

# Register your models here.

admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Turma)