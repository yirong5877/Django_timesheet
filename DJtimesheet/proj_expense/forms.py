from django import forms
from .models import proj_expense

class create_projexp_form(forms.ModelForm):
    class Meta:
        model=proj_expense
        fields = ['ExpDescription','ExpBillingCode','ExDefaultRates','ExpActive']
    