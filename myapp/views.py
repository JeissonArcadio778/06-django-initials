from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from .models import Task, Project


# Create your views here.

def hello_world(request):
    title = 'Hello World from Django code'
    return render(request, "index.html", {
        'title' : title
    })

def about(request):
    return HttpResponse("<h1>About<h1>")

def params(request, username):
    print('Username', username)
    # Send the parameter by HttpResponse
    return HttpResponse("<h1>Hello by params %s <h1>" % username)


# Manipulate data
def projects(request):
    projects = Project.objects.all()
    return render(request,'projects.html', {
        'projects': projects
    })

# Return like JSON
# def projects(request):
#     po = list(Project.objects.values())
#     return JsonResponse(po, safe=False)

def tasks(request):

    tasks = Task.objects.all()
    return render(request,'tasks.html', {
        'tasks': tasks
    })

