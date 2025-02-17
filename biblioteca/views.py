from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from biblioteca.models import Aluno, Livro, Emprestimo

from biblioteca.serializers import AlunoSerializer, LivroSerializer, EmprestimoSerializer

# Create your views here.

class AlunoViewSet(ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class EmprestimoViewSet(ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer