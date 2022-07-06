from django.urls import path

from . import views
urlpatterns = [
    path("", views.supplies_code_page, name="supplies_code_page"),
]