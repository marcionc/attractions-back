from core.models import BaseModelMixin
from django.db import models
from django.contrib.auth.models import User

class Rating(BaseModelMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
