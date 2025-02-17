from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
    
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    valor = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.cliente}'
    
class ItensPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()
    valor = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.pedido} - {self.produto}'
    
