from django.db import models

# Create your models here.

class Pais(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.nome} ({self.sigla})"
    
    class Meta:
        verbose_name_plural = "Paises"

class Estado(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=4)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nome} ({self.sigla})"

class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nome} ({self.estado.sigla})"
    
class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField()
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nome} {self.sobrenome} ({self.email})"