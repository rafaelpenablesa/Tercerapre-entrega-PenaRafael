from django import forms
from .models import Libro, Prestatario, Prestamo


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'fecha_donacion', 'condicion', 'nombre_donante']

class PrestatarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  
    class Meta:
        model = Prestatario
        fields = ['nombre', 'email', 'password']

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['prestatario', 'fecha_prestamo', 'fecha_devolucion']

class BuscarForm(forms.Form):
    query = forms.CharField(label='Buscar libros', max_length=200)
