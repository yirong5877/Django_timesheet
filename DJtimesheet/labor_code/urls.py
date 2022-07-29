
from django.urls import path
from . import views
urlpatterns = [
    path("", views.show_all_labor.as_view(),name="show_all_labor"),
    path("show_all/",views.show_all_labor.as_view(),name="show_all_labor"),
    path('new_labor/',views.new_labor, name="create_new_labor"),
    path('edit_labor/<int:pk>',views.edit_labor, name="edit_exist_labor"),


]