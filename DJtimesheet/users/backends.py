from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
UserModel = get_user_model()

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):

        if username is None:
            username=kwargs.get(UserModel.USERNAME_FIELD) #USERNAME_FIELD = 'EmailAddress'
        try:
            case_insenstive_username_field='{}__iexact'.format(UserModel.USERNAME_FIELD) #case_insenstive for email field, two consecutive underscores 
            user=UserModel._default_manager.get(**{case_insenstive_username_field:username}) #username='EmailAddress'
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

# class EmailBackend(ModelBackend):
#     def authenticate(self, request, email=None, password=None, **kwargs):
#         if email is None:
#             email=kwargs.get(UserModel.USERNAME_FIELD) #USERNAME_FIELD = 'EmailAddress'
#         try:
#             #case_insenstive_username_field='{}_iexact'.format(UserModel.USERNAME_FIELD) #case_insenstive for email field
#             user=UserModel._default_manager.get(EmailAddress__iexact=email) #username='EmailAddress'
#         except UserModel.DoesNotExist:
#             UserModel().set_password(password)
#         else:
#             if user.check_password(password) and self.user_can_authenticate(user):
#                 return user