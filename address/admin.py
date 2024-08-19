from django.contrib import admin
from address.models import Address
from recyclebin.admin import AdminRecycleBinModelMixin


class AddressAdmin(AdminRecycleBinModelMixin, admin.ModelAdmin):
    list_display = ['address_street', 'address_number']


admin.site.register(Address)
