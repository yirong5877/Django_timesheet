from django.db import models

# Create your models here.


class EquipmentCodeMaintenance(models.Model):

    Deactivate = 0
    Active= 1

    Status=(
        (Deactivate, 'Deactive'),
        (Active, 'Acactive')
    )

    EquipmentCodeID = models.AutoField(primary_key=True)
    ECDescription = models.CharField(max_length=100, blank=False, verbose_name="Equipment Code Class")
    ECBillingCode = models.CharField(max_length=20, blank=False, verbose_name="Billing Codes")
    ECDefaultRates = models.IntegerField(default=16, blank=True, null=True, verbose_name="Default Hourly Rates")
    ECActive = models.BooleanField(default=True, choices=Status, verbose_name="Active Status")
    LastUpdatedBy = models.IntegerField(null=True, blank=True)  # mark for update
    ECDateAdded = models.DateField(auto_now_add=True, verbose_name='Date Added')
    ECDateUpdated = models.DateField(auto_now=True, verbose_name='Date Updated')
    ECDateActivated = models.DateField(null=True, verbose_name='Date Activated')

    dj_equipment_code = models.Manager()

    @property
    def dollar_hourrate(self):
        return f'$ {self.ECDefaultRates} /Hr.'

    @property
    def Active_status(self):
        if self.ECActive:
            show = 'Y'
        else:
            show = 'N'
        return show

    def __str__(self):
        return f"The default hourly rate of {self.ECDescription} is {self.ECDefaultRates}"

