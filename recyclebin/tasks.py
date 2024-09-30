# from recyclebin.models import RecycleBin
# from django.core.serializers import serialize
# import json
#
# def backup_deleted_object(instance, user=None):
#     serialized_data = serialize('json', [instance], use_natural_primary_keys=True, use_natural_foreign_keys=True)
#     deleted_object = json.loads(serialized_data)[0]['fields']
#
#     deleted_by = user.username if user else 'Excluído pelo Sistema'
#
#     RecycleBin.objects.create(
#         deleted_object=deleted_object,
#         deleted_by=deleted_by
#     )
#