from django.db import models

# Create your models here.

class proj_expense(models.Model):
    class Meta:
        db_table = 'proj_expense'

    Deactivate=0
    Active=1
    Status=(
    (Deactivate,'Deactive'),
    (Active,'Acactive')
    )      
    
    expense_code = models.CharField(max_length=100, blank=False,verbose_name = "Project Expense Class")
    billing_code=models.CharField(max_length=20, blank=False,verbose_name = "Billing Codes")
    hourrate= models.IntegerField(default=0)
    Active =models.BooleanField(default=True,choices=Status)
    proj_exp = models.Manager()
    @property
    def dollar_hourrate(self):
        return f'$ {self.hourrate}/Hr.' if self.hourrate else ""
