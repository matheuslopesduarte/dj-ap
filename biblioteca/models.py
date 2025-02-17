from django.db import models

# Create your models here.

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    ano = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.titulo}"
    
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20)
    curso = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Emprestimo(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT)
    data_inicio = models.DateField()
    data_fim = models.DateField()

    def __str__(self):
        return f'{self.aluno} - {self.livro} - {self.data_inicio} - {self.data_fim}'