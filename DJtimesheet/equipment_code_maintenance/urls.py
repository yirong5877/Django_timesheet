from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.ShowAllEquipmentCode.as_view(), name='show_all_equipment_codes'),
    path('list_all_equipment_codes/', views.EquipmentCodeListView.as_view(), name='list_all_equipment_codes'),
    path('create_new_equipment_code/', views.EquipmentCodeCreateView.as_view(), name='create_new_equipment_code'),
    path('adjust_existing_equipment_code/<int:pk>/', views.EquipmentCodeUpdateView.as_view(),
         name='adjust_existing_equipment_code'),
]