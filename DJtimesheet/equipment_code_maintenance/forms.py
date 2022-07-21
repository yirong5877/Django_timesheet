from django import forms
from .models import EquipmentCodeMaintenance


class NewEquipmentCodeForm(forms.ModelForm):
    class Meta:
        model = EquipmentCodeMaintenance
        fields = ['ECDescription', 'ECBillingCode', 'ECDefaultRates', 'ECActive']

