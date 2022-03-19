from multiprocessing import context
from django.shortcuts import render


projectList = [
  {
    'id': '1',
    'title': 'Ecommerce Website',
    'description': 'Fully functional blah'    
  },
  {
      'id': '2',
      'title': 'Portafolio Website',
      'description': 'A personal blah'
  },
  {
      'id': '3',
      'title': 'Social Network',
      'description': 'An open source blah'
  },
]


def projects(request):
    name = 'Dennis Ivanov'

    context = {'projects': projectList}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObject = None
    for i in projectList:
      if i['id'] == str(pk):
        projectObject = i
    
    context = {'project': projectObject}
    return render(request, 'projects/singleProject.html', context)
  