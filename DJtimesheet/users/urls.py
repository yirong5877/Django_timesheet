from django.urls import path
from . import views
from .views import new_user_view
urlpatterns = [
    path("", views.signin, name="xiao_login"),
    path("after_signin/", views.after_signin, name="after_signin"),
    path("login/", views.signin, name="xiao_login"),
    path("signout/", views.signout, name="xiao_signout"),
    path("users/new_user/", new_user_view.as_view(), name='create_new_user'),
    path("sendemail/", views.send_email, name="sendemail"),
    path(
        "users/show_all/",
        views.ShowAll_users.as_view(),
        name="show_all_users",
    ),
]