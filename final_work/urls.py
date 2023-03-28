"""final_work URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from taskmanager.views import *
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view


urlpatterns = [
    path('', redirect_view ),
    path("admin/", admin.site.urls),
    path("tasklist/", MyModelListView.as_view()),
    path("taskupdate/<int:pk>", MyModelUpdateView.as_view()),
    path("taskcreate/", MyModelCreateView.as_view()),
    path("taskdelete/<int:pk>", MyModelDeleteView.as_view()),
    path("taskdetail/<int:pk>", MyModelDetailView.as_view()),
    path("sprintlist/", SprintListView.as_view()),
    path("sprintupdate/<int:pk>", SprintUpdateView.as_view()),
    path("sprintcreate/", SprintCreateView.as_view()),
    path("sprintdelete/<int:pk>", SprintDeleteView.as_view()),
    path("sprintdetail/<int:pk>", SprintDetailView.as_view()),
    path("projectlist/", ProjectListView.as_view()),
    path("projectupdate/<int:pk>", ProjectUpdateView.as_view()),
    path("projectcreate/", ProjectCreateView.as_view()),
    path("projectdelete/<int:pk>", ProjectDeleteView.as_view()),
    path("projectdetail/<int:pk>", ProjectDetailView.as_view()),
    path("api/", include("taskmanager.urls")),
]
