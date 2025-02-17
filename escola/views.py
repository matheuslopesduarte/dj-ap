from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from escola.models import Aluno, Professor, Turma

from escola.serializers import AlunoSerializer, ProfessorSerializer, TurmaSerializer

# Create your views here.

class AlunoViewSet(ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class ProfessorViewSet(ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class TurmaViewSet(ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer