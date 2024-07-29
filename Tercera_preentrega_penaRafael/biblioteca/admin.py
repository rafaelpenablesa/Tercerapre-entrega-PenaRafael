from django.contrib import admin
from .models import Libro, Prestatario, Prestamo

class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_donacion', 'condicion', 'nombre_donante')
    list_filter = ('condicion',)
    search_fields = ('titulo', 'autor')

class PrestatarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email')
    search_fields = ('nombre', 'email')

class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('libro', 'prestatario', 'fecha_prestamo', 'fecha_devolucion')
    list_filter = ('fecha_prestamo', 'fecha_devolucion')
    search_fields = ('libro__titulo', 'prestatario__nombre')

admin.site.register(Libro, LibroAdmin)
admin.site.register(Prestatario, PrestatarioAdmin)
admin.site.register(Prestamo, PrestamoAdmin)
