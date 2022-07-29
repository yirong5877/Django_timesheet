from django.urls import path, include
from . import views


urlpatterns = [
    path('home/', views.ShowAllSuppliesCode.as_view(), name='show_all_supplies_codes'),
    path('', views.SuppliesCodeListView.as_view(), name='supplies_codes_home_page'),
    path('create_new_supplies_code/', views.new_supplies_code, name='create_new_supplies_code'),
    path('adjust_supplies_code/<int:pk>/', views.edit_supplies_code,
         name='adjust_existing_supplies_code'),
]