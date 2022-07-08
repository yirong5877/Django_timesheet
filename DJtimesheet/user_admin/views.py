from django.conf.global_settings import SECRET_KEY
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.shortcuts import reverse
from django.views import View



def register_new_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponse("Now you can log-in") # commented
            return HttpResponseRedirect(reverse("useradmin_login")) # New statement
    elif request.method == "GET":
        form = UserCreationForm()
    return render(request, 'user_admin/register_new_user.html', context={'form': form})
