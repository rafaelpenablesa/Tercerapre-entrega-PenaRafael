from django.urls import path
from . import views

urlpatterns = [
    path('crear_autor/', views.crear_autor, name='crear_autor'),
    path('buscar/', views.buscar, name='buscar'),
]
