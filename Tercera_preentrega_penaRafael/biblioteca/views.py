from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro, Prestamo
from .formularios import LibroForm, PrestatarioForm, PrestamoForm, BuscarForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import Prestatario
from django.contrib.auth.decorators import login_required
from django.utils import timezone


def donar_libro(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Gracias por Donar un Libro!')
            return redirect('donar_libro')
    else:
        form = LibroForm()
    return render(request, 'vistas/formulario_libro.html', {'form': form})

def agregar_prestatario(request):
    if request.method == 'POST':
        form = PrestatarioForm(request.POST)
        if form.is_valid():
            
            prestatario = Prestatario.objects.create(
                nombre=form.cleaned_data['nombre'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )   
            messages.success(request, 'Prestatario agregado exitosamente.')
            return redirect('seleccionar_libro_prestamo')

    else:
        form = PrestatarioForm()
    
    return render(request, 'vistas/formulario_prestatario.html', {'form': form})

def seleccionar_libro_prestamo(request):
    # Fetch the IDs of books currently on loan (regardless of fecha_devolucion)
    prestados = Prestamo.objects.values_list('libro_id', flat=True)
    libros_disponibles = Libro.objects.exclude(id__in=prestados)

    return render(request, 'vistas/seleccionar_libro_prestamo.html', {'libros': libros_disponibles})

def seleccionar_libro_devolucion(request):
    libros = Prestamo.objects.filter(fecha_devolucion__isnull=True)
    return render(request, 'vistas/seleccionar_libro_devolucion.html', {'libros': libros})

@login_required
def pedir_prestamo(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    if request.method == "POST":
        form = PrestamoForm(request.POST)
        if form.is_valid():
            prestamo = form.save(commit=False)
            prestamo.libro = libro
            prestamo.usuario = request.user  # Assign the logged-in user to the usuario field
            prestamo.save()
            messages.success(request, f'¡Libro "{libro.titulo}" prestado con éxito!')
            return redirect('seleccionar_libro_prestamo')
    else:
        form = PrestamoForm()
    return render(request, 'vistas/formulario_prestamo.html', {'form': form, 'libro': libro})


@login_required
def registrar_devolucion(request, libro_id):
    prestamo = get_object_or_404(Prestamo, libro__id=libro_id, fecha_devolucion__isnull=True)
    if request.method == "POST":
        prestamo.fecha_devolucion = timezone.now()
        prestamo.save()
        messages.success(request, f'¡Libro "{prestamo.libro.titulo}" devuelto con éxito!')
        return redirect('seleccionar_libro_devolucion')
    return render(request, 'vistas/formulario_devolucion.html', {'prestamo': prestamo})

def buscar(request):
    if request.method == "GET":
        form = BuscarForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            resultados = Libro.objects.filter(titulo__icontains=query)
            return render(request, 'vistas/resultados.html', {'resultados': resultados, 'query': query})
    else:
        form = BuscarForm()
    return render(request, 'vistas/buscar.html', {'form': form})

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'vistas/home.html')