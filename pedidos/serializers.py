from rest_framework.serializers import ModelSerializer
from .models import Pedido, Cliente, ItensPedido

class PedidoSerializer(ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ItensPedidoSerializer(ModelSerializer):
    class Meta:
        model = ItensPedido
        fields = '__all__'