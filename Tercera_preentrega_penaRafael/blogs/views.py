from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import BlogForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def lista_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs/lista_blogs.html', {'blogs': blogs})

def detalle_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blogs/detalle_blog.html', {'blog': blog})

def crear_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_blogs')
    else:
        form = BlogForm()
    return render(request, 'blogs/formulario_blog.html', {'form': form})


def editar_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)

    if blog.autor != request.user:
        messages.error(request, "No tienes permiso para editar este blog.")
        return redirect('lista_blogs')

    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog actualizado exitosamente.')
            return redirect('lista_blogs')
    else:
        form = BlogForm(instance=blog)
    
    return render(request, 'blogs/formulario_blog.html', {'form': form, 'blog': blog})


def eliminar_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)

   
    if blog.autor != request.user:
        messages.error(request, "No tienes permiso para eliminar este blog.")
        return redirect('lista_blogs')

    if request.method == "POST":
        blog.delete()
        messages.success(request, "Blog eliminado exitosamente.")
        return redirect('lista_blogs')
    
    return render(request, 'blogs/eliminar_blog.html', {'blog': blog})