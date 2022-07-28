from django import forms
from .models import proj_expense

class create_projexp_form(forms.ModelForm):
    class Meta:
        model=proj_expense
        fields = ['ExpDescription','ExpBillingCode','ExDefaultRates','ExpActive']
        widgets={
            'ExpDescription':forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Project Expense Class"}),
            'ExpBillingCode':forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Billing Codes"}),
            'ExDefaultRates':forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Default Rates"}),
            'ExpActive':forms.RadioSelect(attrs={"required": "required", "class": "radioset"}),

        }

    