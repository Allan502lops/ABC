# alumnos/urls.py


from django.urls import path
from .views import listar_alumnos, agregar_alumno, editar_alumno, eliminar_alumno, estadisticas_edad

urlpatterns = [
    path('listar/', listar_alumnos, name='listar_alumnos'),
    path('agregar/', agregar_alumno, name='agregar_alumno'),
    path('eliminar/<int:id>/', eliminar_alumno, name='eliminar_alumno'),
    path('editar/<int:id>/', editar_alumno, name='editar_alumno'),
    path('estadisticas/', estadisticas_edad, name='estadisticas_edad'),
]
