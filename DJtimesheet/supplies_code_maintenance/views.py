from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy, reverse

from .forms import NewSuppliesCodeForm
from .models import SuppliesCodeMaintenance

# Create your views here.


class ShowAllSuppliesCode(View):
    template_name = 'supplies_code_maintenance/show_all_supplies_codes.html'
    context_object_name = 'all_supplies_code'

    def get(self, request, *args, **kwargs):
        all_supplies_codes = SuppliesCodeMaintenance.dj_supplies_code.all()
        return render(request, self.template_name, {'all_supplies_codes': all_supplies_codes})


class SuppliesCodeListView(ListView):
    model = SuppliesCodeMaintenance
    ordering = ['SCDescription']
    queryset = SuppliesCodeMaintenance.dj_supplies_code.all()


class SuppliesCodeCreateView(CreateView):
    model = SuppliesCodeMaintenance
    fields = ['SCDescription', 'SCBillingCode', 'SCDefaultRates', 'SCActive']
    success_url = reverse_lazy('show_all_supplies_codes')
    template_name = 'supplies_code_maintenance/create_supplies_code.html'

    def form_valid(self, form):
        if form.instance.SCDefaultRates < 16 or form.instance.SCDefaultRates > 120:
            form.add_error('SCDefaultRates', 'Hourly rate must be between 16 and 120.')
            return self.form_invalid(form)
        return super().form_valid(form)


class SuppliesCodeUpdateView(UpdateView):
    model = SuppliesCodeMaintenance
    fields = ['SCDescription', 'SCBillingCode', 'SCDefaultRates', 'SCActive']
    success_url = reverse_lazy('show_all_supplies_codes')
    template_name = 'supplies_code_maintenance/update_supplies_code.html'

    def form_valid(self, form):
        print("Self.object = ", self.object.SCDescription, self.object.SCBillingCode,
              self.object.SCDefaultRates, self.object.SCActive)
        print("form.instance = ", form.instance.SCDescription, form.instance.SCBillingCode,
              form.instance.SCDefaultRates, form.instance.SCActive)
        print("form.initial = ", form.initial)
        print("form.cleaned_data = ", form.cleaned_data)

        if form.instance.SCDefaultRates < 16 or form.instance.SCDefaultRates > 120:
            form.add_error('SCDefaultRates', 'Hourly rate must be between 16 and 120.')
            return self.form_invalid(form)
        return super().form_valid(form)


def new_supplies_code(request):
    form = NewSuppliesCodeForm()
    if request.method == 'POST':
        form = NewSuppliesCodeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("show_all_supplies_codes"))

    return render(request, 'supplies_code_maintenance/create_supplies_code.html', {'form':form})


def edit_supplies_code(request, pk):
    a_supplies_code=SuppliesCodeMaintenance.dj_supplies_code.get(SuppliesCodeID=pk)
    form = NewSuppliesCodeForm(instance=a_supplies_code)
    if request.method == 'POST':
        form = NewSuppliesCodeForm(request.POST, instance=a_supplies_code)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("show_all_supplies_codes"))

    context = {'form': form}
    return render(request, 'supplies_code_maintenance/update_supplies_code.html', context)
