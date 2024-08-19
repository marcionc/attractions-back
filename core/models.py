from django.db import models

class BaseModelMixin(models.Model):
    """
    Models com campos base para todos os outros models
    """
    created_date = models.DateTimeField('Criado em', auto_now_add=True, null=True, blank=True)
    updated_date = models.DateTimeField('Atualizado em', auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True

class TouristSpot(BaseModelMixin):
    name = models.CharField('Nome', max_length=150)
    description = models.TextField('Descrição', blank=True)
    approved = models.BooleanField('Está aprovado?', default=False)
    attractions = models.ManyToManyField('attractions.Attraction', blank=True, related_name='attractions')
    comments = models.ManyToManyField('comments.Comment', blank=True, related_name='comments')
    ratings = models.ManyToManyField('ratings.Rating', blank=True, related_name='ratings')
    address = models.ForeignKey('address.Address', on_delete=models.CASCADE, blank=True, null=True)
    photo = models.ImageField(upload_to='tourist_spots/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ponto turístico'
        verbose_name_plural = 'Pontos turísticos'
