# alumnos/forms.py

from django import forms
from .models import Alumno

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['carnet', 'nombres', 'apellidos', 'correo', 'fecha_nacimiento']
