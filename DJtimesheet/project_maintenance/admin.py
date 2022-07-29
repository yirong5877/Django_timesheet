from django.contrib import admin
from .models import ProjectMaintenance

# Register your models here.

admin.site.site_header = "Disaster Recovery Application Administration"


@admin.register(ProjectMaintenance)
class ProjectMaintenanceAdmin(admin.ModelAdmin):
    fields = ['ProjectName', 'ProjectLocation', 'ProjectManager', 'PJDateCreated']
    ordering = ['ProjectName']
    search_fields = ['ProjectName', 'ProjectLocation', 'ProjectManager', 'PJDateCreated']
    list_display =('ProjectName', 'ProjectLocation', 'ProjectManager', 'PJDateCreated') # override list_display to show the list of columns
    list_filter = ('ProjectName', 'ProjectLocation', 'ProjectManager', 'PJDateCreated')