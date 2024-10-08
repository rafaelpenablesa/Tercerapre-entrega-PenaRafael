from django.contrib import admin 
from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('donar_libro/', views.donar_libro, name='donar_libro'),
    path('agregar_prestatario/', views.agregar_prestatario, name='agregar_prestatario'),
    path('seleccionar_libro_prestamo/', views.seleccionar_libro_prestamo, name='seleccionar_libro_prestamo'),
    path('seleccionar_libro_devolucion/', views.seleccionar_libro_devolucion, name='seleccionar_libro_devolucion'),
    path('pedir_prestamo/<int:libro_id>/', views.pedir_prestamo, name='pedir_prestamo'),
    path('registrar_devolucion/<int:libro_id>/', views.registrar_devolucion, name='registrar_devolucion'),
    path('buscar/', views.buscar, name='buscar'),
    path('about/', views.about, name='about'),
    path('accounts/', include('accounts.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),
]