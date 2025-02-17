from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from cadastro.models import Estado

from cadastro.serializers import EstadoSerializer

# Create your views here.

class EstadoViewSet(ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
 