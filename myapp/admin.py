from django.contrib import admin
from .models import Task, Project


# Register your models here. They comes to admin  UI

admin.site.register(Project)
admin.site.register(Task)



