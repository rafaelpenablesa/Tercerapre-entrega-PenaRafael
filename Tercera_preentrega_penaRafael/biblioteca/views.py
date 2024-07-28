from django.shortcuts import render, redirect
from .models import Autor, Libro, Editorial
from .formularios import AutorForm, LibroForm, EditorialForm, BuscarForm

def crear_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_autor')
    else:
        form = AutorForm()
    return render(request, 'vistas/formulario.html', {'form': form})

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
