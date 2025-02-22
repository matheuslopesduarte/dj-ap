# Generated by Django 5.1.5 on 2025-02-17 11:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0002_alter_emprestimo_data_inicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='aluno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='biblioteca.aluno'),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='livro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='biblioteca.livro'),
        ),
    ]
