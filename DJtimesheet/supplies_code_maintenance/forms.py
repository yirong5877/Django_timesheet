from django import forms
from .models import SuppliesCodeMaintenance


class NewSuppliesCodeForm(forms.ModelForm):
    class Meta:
        model = SuppliesCodeMaintenance
        fields = ['SCDescription', 'SCBillingCode', 'SCDefaultRates', 'SCActive']

