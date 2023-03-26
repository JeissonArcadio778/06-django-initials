
from django.contrib import admin
from django.urls import path, include

# Aqui sería el router el proyecto

urlpatterns = [
    path('admin/', admin.site.urls),
    # Ejecucion de mis app URLs de myapp. 
    path('myapp', include('myapp.urls')) # Example: http://127.0.0.1:3000/myapp
]
