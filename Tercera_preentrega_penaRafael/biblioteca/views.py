from django.shortcuts import render, redirect
from .models import Libro
from .formularios import LibroForm, BuscarForm
from django.contrib import messages

def crear_libro(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Gracias por Donar tu libro!')
            return redirect('crear_libro')
    else:
        form = LibroForm()
    return render(request, 'vistas/formulario_libro.html', {'form': form})

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
