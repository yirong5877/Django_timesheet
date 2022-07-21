
from tabnanny import verbose
from django.db import models
#import package for Customer user model
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phone_field import PhoneField




'''
Create a custom Manager, by subclassing BaseUserManager,
that uses an email as the unique identifier instead of a username
Create user with "Standard User" 
Create Superuser with "Internal User"
'''
# Custom UserManager for BaseRole 
class CustomUser_manager(BaseUserManager):
        def _create_user(self, EmailAddress, password, **extra_fields):
        #Initial new User by the given email and password.
            if not EmailAddress:
                raise ValueError('The Email must be set')
            EmailAddress = self.normalize_email(EmailAddress)
            user = self.model(EmailAddress=EmailAddress, **extra_fields)
            user.set_password(password)
            user.save()
            return user
        def create_user(self, EmailAddress, password=None, **extra_fields):
        #Initial new base role User by the given EmailAddress and password.
            extra_fields.setdefault('is_active',False)
            extra_fields.setdefault('is_admin',False)
            extra_fields.setdefault('Userrole','Standard User')
            user = self.model(EmailAddress=EmailAddress, **extra_fields)
            user.set_password(password)
            user.save()
            return user
        def create_superuser(self, EmailAddress, password, **extra_fields):
       # Create and save a SuperUser with the given email and password.
            extra_fields.setdefault('is_active', True)
            extra_fields.setdefault('is_admin',True)
            extra_fields.setdefault('Userrole','Internal User')
            user = self.model(EmailAddress=EmailAddress, **extra_fields)
            user.set_password(password)
            user.save()
            return user



'''
Enable Login with Email in Django
This is for Custom user model
Authentication login with email not username
'''

class CustomUser(AbstractBaseUser):
    class Meta:
        db_table='URI_UserMaintenance'
    class Role(models.TextChoices):
        External = "External User", "Ext_user"
        Internal = "Internal User", "Int_user"
        STAND = "Standard User", "basic_user"
    base_role = Role.STAND
    Userrole = models.CharField(max_length=50, choices=Role.choices)
    UserID=models.AutoField(primary_key=True,editable=False)
    FirstName=models.CharField(max_length=100,blank=True)
    LastName=models.CharField(max_length=100,blank=True)
    PrimaryNumber=PhoneField(blank=True, verbose_name='Contact phone number')
    EmailAddress = models.EmailField(max_length=254, unique=True,verbose_name='Email Address')
    Company=models.CharField(max_length=100, blank=True,verbose_name = "Company Name")
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
 
    date_joined=models.DateField(auto_now_add=True, verbose_name='Created Date')
    date_modified = models.DateField(auto_now=True,verbose_name = "Last Modified Date")
    USERNAME_FIELD = 'EmailAddress'
    REQUIRED_FIELDS = []
    cus_user = CustomUser_manager()
    #objects= CustomUser_manager()


# Initial user role==base role, when create new user 

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


    def __str__(self):
        name=f'{self.FirstName} {self.LastName}' 
        return name
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    @property
    def username(self):
        return f'{self.FirstName} {self.LastName}' 





