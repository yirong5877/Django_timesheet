from django import forms
from .models import ProjectMaintenance


class NewProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectMaintenance
        fields = ['ProjectName', 'ProjectLocation', 'ProjectManager']
