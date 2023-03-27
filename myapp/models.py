from django.db import models

# Create your models here.

# Creación de modelo. Esta es una columna. 
class Project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name 

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    done = models.BooleanField(default=False)
    # Relation
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title + ' - ' + self.project.name

