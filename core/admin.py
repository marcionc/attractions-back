from django.contrib import admin
from core.models import TouristSpot

class TouristSpotAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'approved')


admin.site.register(TouristSpot, TouristSpotAdmin)
