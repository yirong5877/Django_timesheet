from ftplib import all_errors
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from django.shortcuts import render
from datetime import date
from django.db import connection
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
# proj_expense_home_page view

def  exp_home_page(request):
    return render(request,'proj_expense/Home_page.html')

# def  exp_home_page(request):
#     return render(request,'DJtimesheet/blank_page.html')