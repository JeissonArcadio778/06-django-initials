from django.urls import path
from . import views


urlpatterns = [
    path('', views.hello_world, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('params/<str:username>', views.params, name = 'params'),
    path('projects/', views.projects, name =' projects'),
    path('tasks/', views.tasks, name = 'tasks'),
    # path('tasks/<int:id>', views.tasks),
    path('create_task/', views.create_task, name = 'create_task' ),
    path('create_project/', views.create_project, name = 'create_project'),

]