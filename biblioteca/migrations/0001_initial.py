# Generated by Django 5.1.5 on 2025-02-17 11:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('matricula', models.CharField(max_length=20)),
                ('curso', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=100)),
                ('ano', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField(auto_now_add=True)),
                ('data_fim', models.DateField()),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.aluno')),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.livro')),
            ],
        ),
    ]
