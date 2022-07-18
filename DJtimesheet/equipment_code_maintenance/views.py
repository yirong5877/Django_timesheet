from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy, reverse

from .forms import NewEquipmentCodeForm
from .models import EquipmentCodeMaintenance

# Create your views here.


class ShowAllEquipmentCode(View):
    template_name = 'equipment_code_maintenance/show_all_equipment_codes.html'
    context_object_name = 'all_equipment_code'

    def get(self, request, *args, **kwargs):
        all_equipment_codes = EquipmentCodeMaintenance.dj_equipment_code.all()
        return render(request, self.template_name, {'all_equipment_codes': all_equipment_codes})


class EquipmentCodeListView(ListView):
    model = EquipmentCodeMaintenance
    ordering = ['ECDescription']
    queryset = EquipmentCodeMaintenance.dj_equipment_code.all()


class EquipmentCodeCreateView(CreateView):
    model = EquipmentCodeMaintenance
    fields = ['ECDescription', 'ECBillingCode', 'ECDefaultRates', 'ECActive']
    success_url = reverse_lazy('show_all_equipment_codes')
    template_name = 'equipment_code_maintenance/create_equipment_code.html'

    def form_valid(self, form):
        if form.instance.ECDefaultRates < 16 or form.instance.ECDefaultRates > 120:
            form.add_error('ECDefaultRates', 'Hourly rate must be between 16 and 120.')
            return self.form_invalid(form)
        return super().form_valid(form)


class EquipmentCodeUpdateView(UpdateView):
    model = EquipmentCodeMaintenance
    fields = ['ECDescription', 'ECBillingCode', 'ECDefaultRates', 'ECActive']
    success_url = reverse_lazy('show_all_equipment_codes')
    template_name = 'equipment_code_maintenance/update_equipment_code.html'

    def form_valid(self, form):
        print("Self.object = ", self.object.ECDescription, self.object.ECBillingCode,
              self.object.ECDefaultRates, self.object.ECActive)
        print("form.instance = ", form.instance.ECDescription, form.instance.ECBillingCode,
              form.instance.ECDefaultRates, form.instance.ECActive)
        print("form.initial = ", form.initial)
        print("form.cleaned_data = ", form.cleaned_data)

        if form.instance.ECDefaultRates < 16 or form.instance.ECDefaultRates > 120:
            form.add_error('ECDefaultRates', 'Hourly rate must be between 16 and 120.')
            return self.form_invalid(form)
        return super().form_valid(form)


def new_equipment_code(request):
    form = NewEquipmentCodeForm()
    if request.method == 'POST':
        form = NewEquipmentCodeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("show_all_equipment_codes"))

    return render(request, 'equipment_code_maintenance/create_equipment_code.html', {'form':form})


def edit_equipment_code(request, pk):
    a_equipment_code=EquipmentCodeMaintenance.dj_equipment_code.get(EquipmentCodeID=pk)
    form = NewEquipmentCodeForm(instance=a_equipment_code)
    if request.method == 'POST':
        form=NewEquipmentCodeForm(request.POST, instance=a_equipment_code)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("show_all_equipment_codes"))

    context = {'form': form}
    return render(request,'equipment_code_maintenance/update_equipment_code.html', context)
