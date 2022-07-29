from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy, reverse

from .forms import NewProjectForm
from .models import ProjectMaintenance

# Create your views here.


class ShowAllProject(View):
    template_name = 'project_maintenance/show_all_projects.html'
    context_object_name = 'all_project'

    def get(self, request, *args, **kwargs):
        all_projects = ProjectMaintenance.dj_project_maintenance.all()
        return render(request, self.template_name, {'all_projects': all_projects})


class ProjectCreateView(CreateView):
    model = ProjectMaintenance
    fields = ['ProjectName', 'ProjectLocation', 'ProjectManager', 'PJDateCreated']
    success_url = reverse_lazy('show_all_projects')
    template_name = 'project_maintenance/create_project.html'


class ProjectUpdateView(UpdateView):
    model = ProjectMaintenance
    fields = ['ProjectName', 'ProjectLocation', 'ProjectManager', 'PJDateCreated']
    success_url = reverse_lazy('show_all_projects')
    template_name = 'project_maintenance/update_project_info.html'

    def form_valid(self, form):
        print("Self.object = ", self.object.ProjectName,
              self.object.ProjectLocation, self.object.ProjectManager, self.object.PJDateCreated)
        print("form.instance = ", form.instance.ProjectName,
              form.instance.ProjectLocation, form.instance.ProjectManager, form.instance.PJDateCreated)
        print("form.initial = ", form.initial)
        print("form.cleaned_data = ", form.cleaned_data)


def new_project(request):
    form = NewProjectForm()
    if request.method == 'POST':
        form = NewProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("show_all_projects"))

    return render(request, 'project_maintenance/create_project.html', {'form':form})


def edit_project(request, pk):
    a_project=ProjectMaintenance.dj_project_maintenance.get(ProjectID=pk)
    form = NewProjectForm(instance=a_project)
    if request.method == 'POST':
        form=NewProjectForm(request.POST, instance=a_project)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("show_all_projects"))

    context = {'form': form}
    return render(request, 'project_maintenance/update_project_info.html', context)
