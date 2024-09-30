# Generated by Django 5.0.7 on 2024-07-16 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='address_number',
            field=models.CharField(default=82, max_length=50, verbose_name='Número'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='address',
            name='address_city',
            field=models.CharField(max_length=150, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='address',
            name='address_country',
            field=models.CharField(max_length=70, verbose_name='País'),
        ),
        migrations.AlterField(
            model_name='address',
            name='address_state',
            field=models.CharField(max_length=50, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='address',
            name='address_street',
            field=models.CharField(max_length=150, verbose_name='Rua'),
        ),
        migrations.AlterField(
            model_name='address',
            name='address_zip',
            field=models.CharField(max_length=50, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='address',
            name='latitude',
            field=models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Latitude'),
        ),
        migrations.AlterField(
            model_name='address',
            name='longitude',
            field=models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Longitude'),
        ),
    ]
