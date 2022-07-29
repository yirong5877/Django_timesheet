from django.db import models
from datetime import date


# Create your models here.


class ProjectMaintenance(models.Model):
    ProjectID = models.AutoField(primary_key=True)
    ProjectName = models.CharField(max_length=100, blank=False, verbose_name="Project Name")
    ProjectLocation = models.CharField(max_length=128, blank=True, null=True, verbose_name="Project Location",
                                       help_text="(Street, City, State and Zip code)") # mark for update
    ProjectDuration = models.DurationField(blank=True, verbose_name="Project Duration")
    ProjectManager = models.IntegerField(null=True, blank=True, verbose_name="Project Manager")  # mark for update; Project Manager (This will be a dropdown showing first name, last name of all the internal admin users).
    PJDateCreated = models.DateField(auto_now_add=True, verbose_name='Date Created')
    PJLastModifiedOn = models.DateField(auto_now=True, verbose_name='Date Modified')
    LastUpdatedBy = models.IntegerField(null=True, blank=True)  # mark for update

    dj_project_maintenance = models.Manager()

    def project_number(self):
        current_year=date.today().year
        return f'{str(current_year)}-000{self.ProjectID}'

    def __str__(self):
        return f"{self.ProjectName} is created on {self.PJDateCreated} and managed by {self.ProjectManager}"

