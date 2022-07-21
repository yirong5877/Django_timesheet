from django.urls import path
from . import views
urlpatterns = [
    path("",  views.ShowAll_projexpense.as_view(),
        name="show_all_expense",),
     path(
        "show_all/",
        views.ShowAll_projexpense.as_view(),
        name="show_all_expense",
    ),
    path('new_projexp/',views.new_projexpense, name="create_new_projexp"),
    path('edit_projexp/<int:pk>',views.edit_projexpense, name="edit_exist_projexp"),



]