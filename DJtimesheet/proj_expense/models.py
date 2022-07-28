from django.db import models

# Create your models here.
   
class proj_expense(models.Model):
    class Meta:
        db_table = 'URI_projexpense'

    Deactivate=0
    Active=1
    Status=(
    (Deactivate,'Deactive'),
    (Active,'Acactive')
    )      
    
    ExpenseCodeID=models.AutoField(primary_key = True)
    ExpDescription = models.CharField(max_length=100, blank=False,verbose_name = "Project Expense Class")
    ExpBillingCode=models.CharField(max_length=20, blank=False,verbose_name = "Billing Codes")
    ExDefaultRates= models.IntegerField(default=0, blank=True,null=True,verbose_name = "Default Rate")
    ExpActive =models.BooleanField(default=True,choices=Status,verbose_name = "Active Status")
    LastUpdatedBy=models.IntegerField(null=True,blank=True)#mark for update
    proj_exp = models.Manager()
    @property
    def dollar_hourrate(self):
        return f'$ {self.ExDefaultRates:3} /Hr.' 
    @property
    def Active_status(self):
            if self.ExpActive:
                show='Y'
            else:
                show='N'
            return show
