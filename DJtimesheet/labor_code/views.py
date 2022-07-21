from django.shortcuts import render,redirect
from django.views import View
from .forms import create_labor_form
from .models import *
# Create your views here.

'''
def labor_home_page(request):
    return render(request,'labor_code/home_page.html')
'''


class show_all_labor(View):
    template_name='labor_code/show_all.html'
    def get(self,request, *args, **kwargs):
        labor=labor_code.labor_code.all()
        return render(request,self.template_name,{"all_labor":labor})


def new_labor(request):
    form=create_labor_form()
    if request.method=='POST':
        form=create_labor_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/labor/show_all/')

    context={'form':form}
    return render(request,'labor_code/new_labor.html',context)

def edit_labor(request,pk):
    labor=labor_code.labor_code.get(LaborCodeID=pk)
    form=create_labor_form(instance=labor)
    if request.method=='POST':
        form=create_labor_form(request.POST,instance=labor)
        if form.is_valid():
            form.save()
            return redirect('/labor/show_all/')
    context={'form':form}
    return render(request,'labor_code/new_labor.html',context)



'''
from datetime import date

from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from .models import labor_code


class AddNewLaborCodeCreateView(CreateView):
    model = labor_code
    context_object_name = 'labor_code'
    fields = ['labor_code_id', 'labor_class', 'lc_billing_code', 'lc_hourrate', 'lc_active', 'last_updated_by']
    success_url = reverse_lazy('add_new_lc.html')


    def form_valid(self, form):
        if form.instance.lc_hourrate < 10 or form.instance.lc_hourrate > 120:
            form.add_error('lc_hourrate', 'lc_hourrate must be between 10 and 120.')
            return self.form_invalid(form)
        return super().form_valid(form)


class LaborCodeUpdateView(UpdateView):
    model = labor_code
    context_object_name = 'labor_code'
    fields = ['labor_code_id', 'labor_class', 'lc_billing_code', 'lc_hourrate', 'lc_active', 'last_updated_by']
    success_url = reverse_lazy('view_class_all_labor_code.html')

    def form_valid(self, form):
        print("Self.object = ", self.object.labor_code_class, self.object.lc_billing_code, self.object.last_updated_by,
              self.object.lc_hourrate, self.object.lc_active)
        print("form.instance = ", form.instance.labor_code_class, form.instance.lc_billing_code,
              form.instance.last_updated_by, form.instance.lc_hourrate, form.instance.lc_active)
        print("form.initial = ", form.initial)
        print("form.cleaned_data = ", form.cleaned_data)

        if form.instance.lc_hourrate < 10 or form.instance.lc_hourrate > 120:
            form.add_error('lc_hourrate', 'lc_hourrate must be between 10 and 120.')
            return self.form_invalid(form)
        return super().form_valid(form)
'''


'''
@login_required
def add_new_course(request):
    if request.method == "POST":
        print(request.POST)
        form = NewCourse(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            if obj.course_active_status == 'A':
                obj.course_active_on = date.today().isoformat()
            elif obj.course_active_status == 'I':
                obj.course_active_on = None
            obj.save()
            messages.success(request, f"New course on {obj.course_name} is now available") # New change here.
            return HttpResponseRedirect(reverse("courses_index_page"))
    elif request.method == "GET":
        form = NewCourse()
    return render(request, "courses/add_new_course.html", {'form': form})
'''