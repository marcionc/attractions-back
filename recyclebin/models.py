# from django.db import models
#
# class RecycleBin(models.Model):
#     deleted_object = models.JSONField('Objeto Excluído', blank=True)
#     deleted_by = models.CharField('Excluído por', max_length=255, null=True, blank=True)
#
#     def __str__(self):
#         return f'DEL-OBJ - {self.id}'
#
#     class Meta:
#         verbose_name = 'Objeto Deletado'
#         verbose_name_plural = 'Objetos Deletados'
#
#
# class RecycleBinModelMixin(models.Model):
#     class Meta:
#         abstract = True
#
#     def set_delete_user(self, user):
#         self._delete_user = user
