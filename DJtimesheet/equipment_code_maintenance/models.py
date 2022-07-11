from django.db import models

# Create your models here.

# 1. Create a new Equipment code by providing following information:
    # a. Equipment Code (Mandatory field, up to 100 characters)
    # b. Billing Code (Which will be used on Timecard. Mandatory field, up to 20 characters)
    # c. Default Hourly Rates(if any)
    # d. Active(Default will be true)

class EquipmentCode(models.Model):
    # class Meta:
        # db_table = 'Equipment Code Maintenance'
        # verbose_name_plural = "Equipment Codes"

    ACTIVE_STATUS = [('Y', 'Active'),
                     ('N', 'Inactive'),
                    ]
    equipment_code_class = models.CharField(max_length=100, blank=False)
    billing_code = models.CharField(max_length=20, blank=False)
    # hourly_rate = models.DecimalField(max_digits=5, decimal_places=2, default='$16/Hr')
    hourly_rate = models.IntegerField(default='$16/Hr')
    active = models.CharField(max_length=1, choices=ACTIVE_STATUS, default='Y')
    date_added = models.DateField(verbose_name='date added', auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    date_active = models.DateField(null=True)

    dj_equipment_code = models.Manager()

    def __str__(self):
        return f"Hourly rate of {self.equipment_code_class} is {self.hourly_rate}"



