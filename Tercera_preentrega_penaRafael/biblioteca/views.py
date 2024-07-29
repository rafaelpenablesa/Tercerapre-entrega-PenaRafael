from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro
from .formularios import LibroForm, PrestamoForm, DevolucionForm, BuscarForm
from django.contrib import messages

def donar_libro(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            libro = form.save()
            messages.success(request, '¡Gracias por Donar un Libro!')
            return redirect('donar_libro')
    else:
        form = LibroForm()
    return render(request, 'vistas/formulario_libro.html', {'form': form})

def seleccionar_libro_prestamo(request):
    libros = Libro.objects.all()
    return render(request, 'vistas/seleccionar_libro_prestamo.html', {'libros': libros})

def seleccionar_libro_devolucion(request):
    libros = Libro.objects.all()
    return render(request, 'vistas/seleccionar_libro_devolucion.html', {'libros': libros})

def pedir_prestamo(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    if request.method == "POST":
        form = PrestamoForm(request.POST)
        if form.is_valid():
            # Guardar la información del préstamo (no en la base de datos en este ejemplo)
            messages.success(request, f'¡Libro "{libro.titulo}" prestado a {form.cleaned_data["prestatario"]}!')
            return redirect('pedir_prestamo', libro_id=libro.id)
    else:
        form = PrestamoForm()
    return render(request, 'vistas/formulario_prestamo.html', {'form': form, 'libro': libro})

def registrar_devolucion(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    if request.method == "POST":
        # Registrar la devolución del libro (no en la base de datos en este ejemplo)
        libro.prestatario = ''
        libro.fecha_prestamo = None
        libro.prestado = False
        libro.save()
        messages.success(request, f'¡Libro "{libro.titulo}" devuelto con éxito!')
        return redirect('registrar_devolucion', libro_id=libro.id)
    else:
        form = DevolucionForm()
    return render(request, 'vistas/formulario_devolucion.html', {'form': form, 'libro': libro})

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
