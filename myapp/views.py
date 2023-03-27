from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Task, Project
from .forms import CreateNewTask, CreateNewProject

# Create your views here.


def hello_world(request):
    title = 'Hello World from Django code'
    return render(request, "index.html", {
        'title': title
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
    return render(request, 'projects/projects.html', {
        'projects': projects
    })

# Return like JSON
# def projects(request):
#     po = list(Project.objects.values())
#     return JsonResponse(po, safe=False)


def tasks(request):

    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })


def create_task(request):

    # print(request.GET['description'])

    if request.method == 'GET':

        return render(request, 'tasks/create_task.html', {
            "form": CreateNewTask()
        })
    else:
        Task.objects.create(
            title=request.POST['title'], description=request.POST['description'], project_id=1)
        return redirect('tasks')


def create_project(request):

    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            "form": CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')