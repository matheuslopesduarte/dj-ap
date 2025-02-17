from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from pedidos.models import Cliente, Pedido, ItensPedido

from pedidos.serializers import ClienteSerializer, PedidoSerializer, ItensPedidoSerializer

# Create your views here.

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class ItensPedidoViewSet(ModelViewSet):
    queryset = ItensPedido.objects.all()
    serializer_class = ItensPedidoSerializer