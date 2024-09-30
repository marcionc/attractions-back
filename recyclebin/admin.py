# from django.contrib import admin
# from recyclebin.models import RecycleBin
#
# class AdminRecycleBinModelMixin(admin.ModelAdmin):
#     def delete_model(self, request, obj):
#         # Atribui o usuário que está realizando a exclusão ao objeto
#         obj._delete_user = request.user
#         super().delete_model(request, obj)
#
#     def delete_queryset(self, request, queryset):
#         for obj in queryset:
#             if hasattr(obj, 'set_delete_user'):
#                 obj.set_delete_user(request.user)
#             obj.delete()
#
#
# admin.site.register(RecycleBin)
