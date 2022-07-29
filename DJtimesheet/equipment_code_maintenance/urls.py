from django.urls import path, include
from . import views


urlpatterns = [
    path('home/', views.ShowAllEquipmentCode.as_view(), name='equipment_codes_home_page'),
    path('', views.ShowAllEquipmentCode.as_view(), name='show_all_equipment_codes'),
    path('create_new_equipment_code/', views.new_equipment_code, name='create_new_equipment_code'),
    path('adjust_equipment_code/<int:pk>/', views.edit_equipment_code,
         name='adjust_existing_equipment_code'),
    path('change_active_status/<int:pk>/', views.ChangeActiveStatusView.as_view(), name='change_active_status'),
]