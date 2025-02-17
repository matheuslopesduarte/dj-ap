from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from hospital.models import Paciente, Medico, Consulta

from hospital.serializers import PacienteSerializer, MedicoSerializer, ConsultaSerializer

# Create your views here.

class PacienteViewSet(ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class MedicoViewSet(ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class ConsultaViewSet(ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer