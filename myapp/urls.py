from django.urls import path
from . import views


urlpatterns = [
    path('', views.hello_world),
    path('about/', views.about),
    path('params/<str:username>', views.params),
    path('projects/', views.projects),
    path('tasks/', views.tasks),
    # path('tasks/<int:id>', views.tasks),

]