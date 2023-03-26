# 01-django-initials

```sh

```
# Create virtual environment
python3 -m venv env
# Activate virtual environment
source env/bin/activate
# Deactivate virtual environment
deactivate
# Generate requirements.txt
pip freeze > requirements.txt
# Install requirements
pip install -r requirements.txt

## Django install

```sh
pip install django
```

## Verificar instación

```sh
django-admin --version
```

# Create new Project:

```sh
django-admin startproject django_py_initials . 
```

## Running

```sh
python3 manage.py runserver 8080
```

# Estructura del proyecto:

## db.sqlite3 

Es una DB por defecto que usa Django. BD SQL que funciona como archivos. Flujos de autenticación, datos iniciales. 

## manage.py

Se usa como archivo de comandos administrativos

### Ver ayudas

```sh
python3 manage.py --help 
```

## mySite (modulo de python)

Simplemente es un módulo de python. __pycache__: Relacionada con el caché y la optimización del funcionamiento. 

### settings.py 

Es la config del proyecto. 

*Revisar archivo*


## urls.py 

Son las rutas. 


## asgi.py & wsgi

Se relacionan más a la ejecucion del proyecto. 

# Aplicaciones en Django


Los proyectos están conformados por aplicaciones.

Ejemplo: un proyecto con autenticación, blog, compras, etc. Cada uno de estos se puede dividir en aplicaciones. 

    project {
        app{
            funcionalidades*
        }
        app {
            funcionalidades*
        }
        app {
            funcionalidades*
        }
    }

## Crear aplicaciones

```sh
python3 manage.py startapp blog 
python3 manage.py startapp store 
python3 manage.py startapp task

```
En estas defino las funcionalidades y las acoplo a la APP principal, my site. 


## Estructura App


- views.py (archivo principal): que se le enviará al cliente para visualizar

- admin.py: añadir las aplicaciones al panel de administrador. Crear datos, usuarios, roles, actualizar. 

- migrations: se actualizará mediante la actualización de la DB. Son archivos creados por ORM. 

- apps.py: config de la app. 

- models.py: crear clases, tablas de SQL. Aqui se usa el ORM. 

- tests.py: testing de las vistas y archivos enviados al cliente. 


# Hello World en Django: 

Desde views: 

```py

from django.http import HttpResponse

def hello_world (request):
    return HttpResponse("Hello World")
```

¿En que ruta se va a ejecutar? 
R/. pasarla a mysite/urls


# Data Base Model

- migrations: actualizar mediante código de python. La migracion genera esas tablas, esas schemas.

```py
python3 manage.py makemigrations
```

## Crear tablas dentro de la DB:

Sirve para construir la base de datos a apartir de los modelos declarados. 
```py
python3 manage.py migrate
```


## Unir myapp con mysite: 

Debo crear un modelo para más operaciones. 

# Django Shell

- Manipulacion de la DB mediante la Shell

## Create data en la DB

```sh
python3 manage.py shell
```
Se abrirá:

```py
from myapp.models import Project, Task
p = Project(name="aplication movil")
p
p.save()

Project.objects.all() # All items
Project.oject.get(id=1) # One item 

Project.oject.get(name="aplication movil") # One item 

# Task

p.task_set.create(title = "descargar IDE")
p.task_set.create(title = "desarrollar login")

p.tesk_set.all()

p.task_set.get(id=1)

# Validation return
Project.objects.filter(name__starswith="aplicacion")

po = Project.objects
po.filter(name_startswith="desarrollar")
```

# Params

Recibir informacion desde el cliente para operarlo. 

```py
 path('params/<str:username>', views.params),
```

# Params y models

```py
def projects(request):
    po = list(Project.objects.values())
    return JsonResponse(po, safe=False)
```

# Django Admin

Es un modulo que sirve para administrar todo el proyecto. 

1. Login:

    - Debo crear un usuario. 
   ```py
    python3 manage.py create superuser
   ```
2. Entrando: 

Usarios y grupos. 

3. Podemos crear projects y tasks.

Usando el admin.py/myapp podemos usarla para implementar nuevas tareas en el admin del proyecto.


# Render

Podemos enviar templates, interfaces más elaboradas. 

```py
def hello_world(request):
    return render(request, "index.html")
```

# Templates pass data

- Modulos de templates: permiten procesar HTMLs, añadirlos, agregar lógica. 

En HTML siempre se verá como String. 

```py
print('Username', username)
    # Send the parameter by HttpResponse
    return HttpResponse("<h1>Hello by params %s <h1>" % username)
```

# Jinja Loops. Recorrer datos/elementos

Motor de plantillas

```html
    {% for project in projects %}
    
    <p> {{project.name}} <p>

    {% endfor %}
```

# Jinja conditions: 

```html
{% if task.done == False %} 🕑 {% else %} ✅ {% endif %} 
```

# Template inheritance 

```html
{% extends 'layouts/base.html' %}

{% block content %}
{% endblock %}
```

# Formularios

Envio de info al server. 

    













