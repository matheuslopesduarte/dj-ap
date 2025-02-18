from django.db import models

# Create your models here.

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    disciplina = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Turma(models.Model):
    nome = models.CharField(max_length=100)
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)
    horario = models.TimeField()

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    martricula = models.IntegerField()
    curso = models.CharField(max_length=100)
    turma = models.ForeignKey(Turma, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome