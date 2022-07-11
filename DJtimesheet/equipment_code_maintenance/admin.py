from django.contrib import admin
from .models import EquipmentCode

# Register your models here.


@admin.register(EquipmentCode)
class EquipmentCodeAdmin(admin.ModelAdmin):
    fields = ['equipment_code_class', 'billing_code', 'hourly_rate', 'active']
    ordering = ['equipment_code_class']
    search_fields = ['equipment_code_class', 'billing_code', 'hourly_rate', 'active']
    exclude = ['active']
    list_display = ('equipment_code_class', 'billing_code', 'hourly_rate', 'active') # override list_display to show the list of columns
    list_filter = ('equipment_code_class', 'active')