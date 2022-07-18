from django.contrib import admin
from .models import EquipmentCodeMaintenance

# Register your models here.

admin.site.site_header = "Disaster Recovery Application Administration"


@admin.register(EquipmentCodeMaintenance)
class EquipmentCodeMaintenanceAdmin(admin.ModelAdmin):
    fields = ['ECDescription', 'ECBillingCode', 'ECDefaultRates', 'ECActive']
    ordering = ['ECDescription']
    search_fields = ['ECDescription', 'ECBillingCode', 'ECDefaultRates', 'ECActive']
    exclude = ['ECActive']
    list_display = ('ECDescription', 'ECBillingCode', 'ECDefaultRates', 'ECActive') # override list_display to show the list of columns
    list_filter = ('ECDescription', 'ECActive')