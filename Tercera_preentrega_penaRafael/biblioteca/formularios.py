from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'fecha_donacion', 'condicion', 'nombre_donante']

class PrestamoForm(forms.Form):
    prestatario = forms.CharField(max_length=200, label='Nombre del Prestatario')
    fecha_prestamo = forms.DateField(label='Fecha de Préstamo')

class DevolucionForm(forms.Form):
    pass

class BuscarForm(forms.Form):
    query = forms.CharField(label='Buscar libros', max_length=200)
