from django.contrib import admin

from .models import Aluno, Emprestimo, Livro

# Register your models here.

admin.site.register(Aluno)
admin.site.register(Emprestimo)
admin.site.register(Livro)