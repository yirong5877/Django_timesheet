from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect 
from django.urls import reverse
from DJtimesheet import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User
from .models import CustomUser
from django.views import View

from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import Create_UserForm

'''
This is for User Login, logout and send_email
'''
def after_signin(request):
    return render(request,'users/after_signin.html')


def signin(request):
    if request.method == 'POST':
        useremail=request.POST['email']
        pass1 = request.POST['password']
        user = authenticate(request,EmailAddress=useremail, password=pass1)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged In Sucessfully!!")
            return redirect (reverse("after_signin"))
        else:
            messages.info(request, 'Email OR password is incorrect')
    return render(request,'users/xiao_login.html')


class new_user_view(CreateView):
    model=CustomUser
    form_class = Create_UserForm
    success_url=reverse_lazy('show_all_users')
    template_name = 'users/new_user.html'
  
def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect(reverse("xiao_login"))

def send_email(request):
    if request.method=="POST":
        email=request.POST['email']
        if User.objects.filter(email=email).exists():
             # Forgot password resend by Email
            subject="Timesheet Application Reset your password"
            message="To initiate the password reset process for your Account xxx@xxx  you ask for reset password"
            from_email = settings.EMAIL_HOST_USER
            to_list = [email]
            send_mail(subject, message, from_email, to_list, fail_silently=True)
            return redirect(reverse("xiao_login"))

    return render(request,'users/sendemail.html')


class ShowAll_users(View):
    template_name='users/Show_all.html'
    def get(self,request, *args, **kwargs):
        users=CustomUser.cus_user.all()
        return render(request,self.template_name,{"all_user":users})



