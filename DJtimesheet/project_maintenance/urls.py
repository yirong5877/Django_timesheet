from django.urls import path, include
from . import views


urlpatterns = [
    path('home/', views.ShowAllProject.as_view(), name='project_maintenance_home_page'),
    path('', views.ShowAllProject.as_view(), name='show_all_projects'),
    path('create_new_project/', views.new_project, name='create_new_project'),
    path('adjust_project/<int:pk>/', views.edit_project, name='adjust_existing_project_info'),
]