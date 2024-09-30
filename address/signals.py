# from rest_framework.utils import json
# from recyclebin.models import RecycleBin, RecycleBinModelMixin
#
#
# from django.db.models.signals import pre_delete
# from django.dispatch import receiver
# from django.core.serializers import serialize
# import json
#
# @receiver(pre_delete)
# def backup_deleted_object(sender, instance, **kwargs):
#     # Verifica se o modelo herda de RecycleBinModelMixin
#     if not issubclass(sender, RecycleBinModelMixin):
#         return
#
#     # Tenta obter o usuário que está deletando o objeto
#     user = getattr(instance, '_delete_user', None)
#     if user is None:
#         print(f"Warning: _delete_user is None for {instance}, sender: {sender}")
#
#     deleted_by = user.username if user else 'Excluído pelo Sistema'
#     # Serializa o objeto deletado
#     serialized_data = serialize('json', [instance], use_natural_primary_keys=True, use_natural_foreign_keys=True)
#     deleted_object = json.loads(serialized_data)[0]['fields']
#
#     # Cria um registro no modelo RecycleBin
#     RecycleBin.objects.create(
#         deleted_object=deleted_object,
#         deleted_by=deleted_by
#     )
