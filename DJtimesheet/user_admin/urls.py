from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register_new_user/', views.register_new_user, name='useradmin_register'),
    path('login/', auth_views.LoginView.as_view(template_name='user_admin/login.html'), name='useradmin_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='useradmin_logout'),
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='user_admin/change_password.html'), name='useradmin_change_password'),

]