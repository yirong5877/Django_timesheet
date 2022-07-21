from django import forms
from .models import CustomUser



from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model



class Create_UserForm(UserCreationForm):
    CHOICES=(('External User','External User'),
         ('Internal User','Internal User'),
         ('Standard User','Standard User')
    )

    FirstName = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "enter First Name"
    }))

    LastName = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "enter Last Name"
    }))

    PrimaryNumber = forms.IntegerField(widget=forms.NumberInput(attrs={
        "class": "input",
        "type": "number",
        "placeholder": "enter Contact Number"
    }))

    EmailAddress = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "input",
        "type": "email",
        "placeholder": "enter email"
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "enter password"
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "re-enter password"
    }))
    Company = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "enter Company Name"
    }))
    Userrole = forms.ChoiceField(widget=forms.RadioSelect,choices=CHOICES)
    
    class Meta:
        model = get_user_model()
        fields = ('FirstName', 'LastName', 'PrimaryNumber','EmailAddress','password1', 'password2','Userrole','Company','is_active')
    
