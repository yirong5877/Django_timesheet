from django.db import models

# Create your models here.


class SuppliesCodeMaintenance(models.Model):
    # class Meta:
    #     db_table = 'equipment_code_maintenance_equipmentcode'
    #     verbose_name_plural = "Equipment Codes"

    Deactivate = 0
    Active = 1

    Status = (
        (Deactivate, 'Deactive'),
        (Active, 'Acactive')
    )

    SuppliesCodeID = models.AutoField(primary_key=True)
    SCDescription = models.CharField(max_length=100, blank=False, verbose_name="Supplies Code Class")
    SCBillingCode = models.CharField(max_length=20, blank=False, verbose_name="Billing Codes")
    SCDefaultRates = models.IntegerField(default=0, blank=True, null=True, verbose_name="Default Hourly Rates")
    SCActive = models.BooleanField(default=True, choices=Status, verbose_name="Active Status")
    LastUpdatedBy = models.IntegerField(null=True, blank=True)  # mark for update
    SCDateAdded = models.DateField(auto_now_add=True, verbose_name='Date Added')
    SCDateUpdated = models.DateField(auto_now=True, verbose_name='Date Updated')
    SCDateActivated = models.DateField(null=True, verbose_name='Date Activated')

    dj_supplies_code = models.Manager()


    @property
    def dollar_hourrate(self):
        return f'$ {self.SCDefaultRates} /Hr.'

    @property
    def Active_status(self):
        if self.SCActive:
            show = 'Y'
        else:
            show = 'N'
        return show

    def __str__(self):
        return f"The default hourly rate of {self.SCDescription} is {self.SCDefaultRates}"
