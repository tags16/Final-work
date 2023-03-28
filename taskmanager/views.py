from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from taskmanager.models import Task, TaskStatus, Sprint, Project
from .serializers import TodoSerializer
from .filters import TodoFilterSet
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.schemas.openapi import AutoSchema


User = get_user_model()
def redirect_view(request):
	return redirect("/tasklist")

class TodolistViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-id')
    serializer_class = TodoSerializer
    filterset_class =  TodoFilterSet

    schema = AutoSchema(
        tags=['Tasks'],
        component_name='Task',
        operation_id_base='Task',
    )

class MyModelListView(ListView):
    model = Task
    template_name = 'todo_list.html'

class MyModelUpdateView(UpdateView):
    model = Task
    fields = [
        'name',
        'dead_line',
        'parent_task',
        'user',
        'status',
        'sprint'
    ]
    object_list = Task.objects.all().order_by('id')
    template_name = 'todo_update_form.html'
    success_url = '/tasklist/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = TaskStatus.objects.all()
        context['users'] = User.objects.all()
        context['sprints'] = Sprint.objects.all().order_by('name')
        return context

class MyModelCreateView(CreateView):
    model = Task
    fields = [
        'name',
        'dead_line',
        'parent_task',
        'user',
        'status'
    ]
    template_name = 'todo_create_form.html'
    success_url = '/tasklist/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = TaskStatus.objects.all()
        context['users'] = User.objects.all()
        return context

class MyModelDeleteView(DeleteView):
    model = Task
    template_name = 'todo_delete_form.html'
    success_url = '/tasklist/'

class MyModelDetailView(DetailView):
    model = Task
    template_name = 'todo_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
    
class SprintListView(ListView):
    model = Sprint
    template_name = 'sprint_list.html'

class SprintUpdateView(UpdateView):
    model = Sprint
    fields = [
        'name',
        'is_active',
        'dead_line',
        'project'
    ]
    object_list = Sprint.objects.all().order_by('created')
    template_name = 'sprint_update_form.html'
    success_url = '/sprintlist/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all().order_by('name')
        return context

class SprintCreateView(CreateView):
    model = Sprint
    fields = [
        'name',
        'dead_line',
    ]
    template_name = 'sprint_create_form.html'
    success_url = '/sprintlist/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context

class SprintDeleteView(DeleteView):
    model = Sprint
    template_name = 'sprint_delete_form.html'
    success_url = '/sprintlist/'

class SprintDetailView(DetailView):
    model = Sprint
    template_name = 'sprint_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class ProjectListView(ListView):
    model = Project
    template_name = 'project_list.html'

class ProjectUpdateView(UpdateView):
    model = Project
    fields = [
        'name',
    ]
    object_list = Project.objects.all().order_by('created')
    template_name = 'project_update.html'
    success_url = '/projectlist/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sprint'] = Task.objects.all().order_by('name')
        return context

class ProjectCreateView(CreateView):
    model = Project
    fields = [
        'name',
    ]
    template_name = 'project_create.html'
    success_url = '/projectlist/'

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project_delete.html'
    success_url = '/projectlist/'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context