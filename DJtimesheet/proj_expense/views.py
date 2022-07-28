from django.shortcuts import render,redirect

from django.views import View
from .forms import create_projexp_form
from .models import *
# Create your views here.

class ShowAll_projexpense(View):
    template_name='proj_expense/Show_all.html'
    def get(self,request, *args, **kwargs):
        expense=proj_expense.proj_exp.all()
        return render(request,self.template_name,{"all_expense":expense})


def new_projexpense(request):
    form=create_projexp_form()
    if request.method=='POST':
        form=create_projexp_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/expense/show_all/')
        
    context={'form':form}
    return render(request,'proj_expense/new_projexpense.html',context)


def edit_projexpense(request,pk):
    expense=proj_expense.proj_exp.get(ExpenseCodeID=pk)
    form=create_projexp_form(instance=expense)
    if request.method=='POST':
        form=create_projexp_form(request.POST,instance=expense)
        if form.is_valid():
            form.save()
            return redirect('/expense/show_all/')
    context={'form':form}
    return render(request,'proj_expense/new_projexpense.html',context)

