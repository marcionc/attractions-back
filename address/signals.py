from django.core.serializers import serialize
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from rest_framework.utils import json
from recyclebin.models import RecycleBin, RecycleBinModelMixin


@receiver(pre_delete)
def backup_deleted_object(sender, instance, **kwargs):
    if not issubclass(sender, RecycleBinModelMixin):
        return

    user = getattr(instance, '_delete_user', None)
    deleted_by = user.username if user else 'Excluído pelo Sistema'

    serialized_data = serialize('json', [instance], use_natural_primary_keys=True, use_natural_foreign_keys=True)
    deleted_object = json.loads(serialized_data)[0]['fields']

    RecycleBin.objects.create(
        deleted_object=deleted_object,
        deleted_by=deleted_by
    )
