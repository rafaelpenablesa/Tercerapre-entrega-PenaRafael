Proyecto Final - Biblioteca Comunal
Comisión: 57815 | Alumno: Rafael Peña

## Descripción
Página web para la administración de una biblioteca comunitaria. Los usuarios pueden donar libros, solicitar préstamos, registrar devoluciones, y publicar reseñas. Es necesario registrarse para acceder a todas las funcionalidades.

## Requisitos
- Python 3.x
- Django

  ## Secciones y Funcionalidades

### Donar un Libro
**Descripción:** Permite a los usuarios agregar nuevos libros al catálogo de la biblioteca.  
**URL:** [http://127.0.0.1:8000/biblioteca/donar_libro/](http://127.0.0.1:8000/biblioteca/donar_libro/)  
**Formulario:**
- Título
- Autor
- Fecha de Donación
- Condición (Mala, Buena, Excelente)
- Nombre del Donante

### Pedir Préstamo de Libro
**Descripción:** Permite seleccionar un libro del catálogo y registrar el préstamo.  
**URL:** [http://127.0.0.1:8000/biblioteca/seleccionar_libro_prestamo/](http://127.0.0.1:8000/biblioteca/seleccionar_libro_prestamo/)  
**Formulario:**
- Prestatario (se asigna automáticamente al usuario logueado)
- Fecha de Préstamo
- Fecha de Devolución (opcional)

### Buscar Libros
**Descripción:** Permite buscar libros en el catálogo de la biblioteca.  
**URL:** [http://127.0.0.1:8000/biblioteca/buscar/](http://127.0.0.1:8000/biblioteca/buscar/)  
**Formulario:**
- Búsqueda (por título del libro)

### Reseñas de Libros
**Descripción:** Los usuarios pueden crear y editar sus propias reseñas de libros.  
**URL:** [http://127.0.0.1:8000/blogs/](http://127.0.0.1:8000/blogs/)

### Ejemplo en Vivo
Para ver una demostración en vivo, visita el siguiente enlace:

**Demo:** [[Ver demo](https://www.loom.com/share/9de121a230724132bf3d372c02758bf2?sid=1c765f08-c7f6-4896-9115-f90d7487e821)](#)

**Casos de prueba:** [[Spreadsheet casos de prueba](https://docs.google.com/spreadsheets/d/1owaQBx_KZhSJWijVBGkkj7Sg4YtTxl1riyiYX9P4xFI/edit?gid=0#gid=0)](#)


## Instalación
1. Clonar el repositorio:
    ```bash
    git clone <[URL_DEL_REPOSITORIO](https://github.com/rafaelpenablesa/Tercerapre-entrega-PenaRafael)>
    cd Tercerapre-entrega+PenaRafael
    ```

2. Crear un entorno virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Instalar dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso
1. Migrar la base de datos:
    ```bash
    python manage.py migrate
    ```
 2. Ejecutar el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```

##Acceso al Panel de Administración

URL: http://127.0.0.1:8000/admin/
**Credenciales predeterminadas:**
    - **Username:** `Admin`
    - **Email address:** `rafaelpenablesa@gmail.com`
    - **Password:** `Admin1234` 





