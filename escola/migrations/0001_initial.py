# Generated by Django 5.1.5 on 2025-02-17 23:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('disciplina', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('horario', models.TimeField()),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.professor')),
            ],
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('martricula', models.IntegerField()),
                ('curso', models.CharField(max_length=100)),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.turma')),
            ],
        ),
    ]
