from django.db import models


# Create your models here.

class labor_code(models.Model):
    class Meta:
        db_table = 'labor_code'

    Deactivate = 0
    Active = 1
    Status = (
        (Deactivate, 'Deactive'),
        (Active, 'Active')
    )

    LaborCodeID = models.AutoField(primary_key = True)
    LCDescription = models.CharField(max_length=100, blank=False, verbose_name="Labor Class")
    LCBillingCode = models.CharField(max_length=20, blank=False, verbose_name="Billing Codes")
    LCDefaultRates = models.IntegerField(default=0, blank=True, null=True, verbose_name="Default Rate")
    LCActive = models.BooleanField(default=True, choices=Status, verbose_name="Active Status")
    LastUpdatedBy = models.CharField(max_length=100, blank=False, default="John")
    #last_updated_by = models.ForeignKey('user_admin.UserProfile', on_delete=models.CASCADE, default='John')
    labor_code = models.Manager()

    '''
    @property
    def dollar_hourrate(self):
        return f'$ {self.hourrate}/Hr.' if self.hourrate else ""
    '''

    @property
    def dollar_hourrate(self):
        return f'$ {self.LCDefaultRates:3} /Hr.'

    @property
    def Active_status(self):
        if self.LCActive:
            show = 'Y'
        else:
            show = 'N'
        return show