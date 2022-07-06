from django.shortcuts import render

# Create your views here.

def  supplies_code_page(request):
    return render(request,'proj_expense/Home_page.html')