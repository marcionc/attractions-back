from django.contrib import admin
from address.models import Address

class AddressAdmin(admin.ModelAdmin):
    list_display = ['address_street', 'address_number']

    # def delete_model(self, request, obj):
    #     backup_deleted_object(obj, request.user)
    #     super().delete_model(request, obj)
    #


admin.site.register(Address)
