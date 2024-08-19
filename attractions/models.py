from core.models import BaseModelMixin
from django.db import models

class Attraction(BaseModelMixin):
    name = models.CharField(max_length=150)
    description = models.TextField('Descrição')
    opening_hours = models.TextField('Horário de Funcionamento')
    minimum_age = models.IntegerField('Idade Minima')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Atração'
        verbose_name_plural = 'Atrações'
