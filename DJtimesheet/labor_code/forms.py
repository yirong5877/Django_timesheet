from django import forms
from .models import labor_code

class create_labor_form(forms.ModelForm):
    class Meta:
        model=labor_code
        fields = ['LCDescription','LCBillingCode','LCDefaultRates','LCActive']
        widgets = {
            'LCDescription': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "Enter Labor Class"}),
            'LCBillingCode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter Billing Codes"}),
            'LCDefaultRates': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter Default Rates"}),
            'LCActive': forms.RadioSelect(attrs={"required": "required", "class": "radioset"}),

        }