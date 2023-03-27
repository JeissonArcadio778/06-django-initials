from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="titulo de tarea", max_length=200)
    description = forms.CharField(label="descripcion de tarea", max_length=1000)

class CreateNewProject(forms.Form):
    name = forms.CharField(label='Ingresa el nombre del formulario', max_length=200)