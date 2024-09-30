from core.models import BaseModelMixin
# from recyclebin.models import RecycleBinModelMixin
from django.db import models

class Address(BaseModelMixin):
    address_street = models.CharField('Rua', max_length=150)
    address_number = models.CharField('Número', max_length=50)
    address_city = models.CharField('Cidade', max_length=150)
    address_state = models.CharField('Estado', max_length=50)
    address_zip = models.CharField('CEP', max_length=50)
    address_country = models.CharField('País', max_length=70)
    latitude = models.DecimalField('Latitude', max_digits=9, decimal_places=2)
    longitude = models.DecimalField('Longitude', max_digits=9, decimal_places=2)

    def __str__(self):
        return f"{self.id}"

    # def delete(self, using=None, keep_parents=False):
    #     # Verifique se o usuário foi atribuído antes da exclusão
    #     if not hasattr(self, '_delete_user'):
    #         # Isso pode ser útil para testes ou exclusões feitas diretamente no código
    #         self._delete_user = None  # Ou defina um valor padrão, se aplicável
    #     super().delete(using=using, keep_parents=keep_parents)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

