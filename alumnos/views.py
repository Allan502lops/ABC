# alumnos/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
from .models import Alumno
from .forms import AlumnoForm
from django.db.models import Count


# Funcion para listar la informacion de un alumno 
def listar_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'alumnos/listar_alumnos.html', {'alumnos': alumnos})

# Funcion para agregar un alumno 
def agregar_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_alumnos')
    else:
        form = AlumnoForm()
    return render(request, 'alumnos/agregar_alumno.html', {'form': form})

# Funcion para editar la informacion de un alumno 
def editar_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)

    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('listar_alumnos')
    else:
        form = AlumnoForm(instance=alumno)

    return render(request, 'alumnos/editar_alumno.html', {'form': form, 'alumno': alumno})

# Funcion para eliminar un alumno 
def eliminar_alumno(request, id):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()
    return redirect('listar_alumnos')

# Funcion para mostrar las estadisticas de los alumnos 
def estadisticas_edad(request):
    estadisticas = Alumno.objects.values('fecha_nacimiento__year').annotate(total=Count('id')).order_by('fecha_nacimiento__year')
    return render(request, 'alumnos/estadisticas_edad.html', {'estadisticas': estadisticas})