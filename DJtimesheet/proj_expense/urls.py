from django.urls import path
from . import views
urlpatterns = [
    path("", views.exp_home_page, name="exp_home_page"),
]