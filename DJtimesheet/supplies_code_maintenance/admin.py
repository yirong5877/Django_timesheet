from django.contrib import admin
from .models import SuppliesCodeMaintenance

# Register your models here.

admin.site.site_header = "Disaster Recovery Application Administration"


@admin.register(SuppliesCodeMaintenance)
class SuppliesCodeMaintenanceAdmin(admin.ModelAdmin):
    fields = ['SCDescription', 'SCBillingCode', 'SCDefaultRates', 'SCActive']
    ordering = ['SCDescription']
    search_fields = ['SCDescription', 'SCBillingCode', 'SCDefaultRates', 'SCActive']
    exclude = ['SCActive']
    list_display = ('SCDescription', 'SCBillingCode', 'SCDefaultRates', 'SCActive') # override list_display to show the list of columns
    list_filter = ('SCDescription', 'SCActive')