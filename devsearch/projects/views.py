from multiprocessing import context
from django.shortcuts import render
from .models import Project


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    reviews = projectObj.review_set.all()
    context = {'project': projectObj, 'tags': tags, 'reviews': reviews}
    return render(request, 'projects/singleProject.html', context)
