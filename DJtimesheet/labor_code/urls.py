'''


from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('add_lc_create_view/', views.AddNewLaborCodeCreateView.as_view(),name='view_class_add_labor_code'),
    path('update_lc_update_view/<int:pk>', views.LaborCodeUpdateView.as_view(), name='view_class_update_laobor_code'),

]
'''

from django.urls import path
from . import views
urlpatterns = [
    path("", views.show_all_labor.as_view(),name="show_all_labor"),
    path("show_all/",views.show_all_labor.as_view(),name="show_all_labor"),
    path('new_labor/',views.new_labor, name="create_new_labor"),
    path('edit_labor/<int:pk>',views.edit_labor, name="edit_exist_labor"),


]