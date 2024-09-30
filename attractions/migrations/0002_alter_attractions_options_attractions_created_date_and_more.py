# Generated by Django 5.0.7 on 2024-07-16 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attractions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attractions',
            options={'verbose_name': 'Atração', 'verbose_name_plural': 'Atrações'},
        ),
        migrations.AddField(
            model_name='attractions',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Criado em'),
        ),
        migrations.AddField(
            model_name='attractions',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Atualizado em'),
        ),
    ]
