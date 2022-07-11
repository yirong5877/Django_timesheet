from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from .models import EquipmentCode

# Create your views here.


class ShowAllEquipmentCode(View):
    template_name = 'equipment_code_maintenance/show_all_equipment_codes.html'

    def get(self, request, *args, **kwargs):
        all_equipment_codes = EquipmentCode.dj_equipment_code.all()
        return render(request, self.template_name, {'all_equipment_codes': all_equipment_codes})


class EquipmentCodeListView(ListView):
    model = EquipmentCode
    ordering = ['equipment_code_class']
    queryset = EquipmentCode.dj_equipment_code.all()


class EquipmentCodeCreateView(CreateView):
    model = EquipmentCode
    fields = ['equipment_code_class', 'billing_code', 'hourly_rate', 'active']
    success_url = reverse_lazy('show_all_equipment_codes')

    def form_valid(self, form):
        if form.instance.hourly_rate < 16 or form.instance.hourly_rate > 120:
            form.add_error('hourly_rate', 'hourly_rate must be between 16 and 120.')
            return self.form_invalid(form)
        return super().form_valid(form)


class EquipmentCodeUpdateView(UpdateView):
    model = EquipmentCode
    fields = ['equipment_code_class', 'billing_code', 'hourly_rate', 'active']
    success_url = reverse_lazy('show_all_equipment_codes')

    def form_valid(self, form):
        print("Self.object = ", self.object.equipment_code_class, self.object.billing_code,
              self.object.hourly_rate, self.object.active)
        print("form.instance = ", form.instance.equipment_code_class, form.instance.billing_code,
              form.instance.hourly_rate, form.instance.active)
        print("form.initial = ", form.initial)
        print("form.cleaned_data = ", form.cleaned_data)

        if form.instance.hourly_rate < 16 or form.instance.hourly_rate > 120:
            form.add_error('hourly_rate', 'hourly_rate must be between 16 and 120.')
            return self.form_invalid(form)
        return super().form_valid(form)
