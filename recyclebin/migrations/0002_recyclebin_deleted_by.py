# Generated by Django 5.0.7 on 2024-07-22 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recyclebin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recyclebin',
            name='deleted_by',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
