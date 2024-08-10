# Proyecto Django Tercera Pre entrega Peña Rafael

## Requisitos
- Python 3.x
- Django

## Instalación
1. Clonar el repositorio:
    ```bash
    git clone <URL_DEL_REPOSITORIO>
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

2. Crear un superusuario:
    ```bash
    python manage.py createsuperuser
    ```

    **Credenciales predeterminadas:**
    - **Username:** `admin`
    - **Email address:** `rafaelpenablesa@gmail.com`
    - **Password:** `adminpassword` (Este es un ejemplo, usa una contraseña segura en producción)

Acceso al Panel de Administración

URL: http://127.0.0.1:8000/admin/

3. Ejecutar el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```

Funcionalidades
Donar un Libro
Permite a los usuarios agregar nuevos libros al catálogo de la biblioteca.

URL: http://127.0.0.1:8000/biblioteca/donar_libro/
Formulario:
Título
Autor
Fecha de Donación
Condición (Mala, Buena, Excelente)
Nombre del Donante

Agregar Prestatario
Permite agregar nuevos prestatarios que pueden pedir libros prestados.

URL: http://127.0.0.1:8000/biblioteca/agregar_prestatario/
Formulario:
Nombre
Email
Pedir Préstamo de Libro
Permite seleccionar un libro del catálogo y registrar el préstamo a un prestatario.

URL: http://127.0.0.1:8000/biblioteca/seleccionar_libro_prestamo/
Formulario:
Prestatario
Fecha de Préstamo
Fecha de Devolución (opcional)
Registrar Devolución de Libro
Permite registrar la devolución de un libro prestado.

URL: http://127.0.0.1:8000/biblioteca/seleccionar_libro_devolucion/
Buscar Libros
Permite buscar libros en el catálogo de la biblioteca.

URL: http://127.0.0.1:8000/biblioteca/buscar/
Formulario:
busqueda (título del libro)

Ejemplos de Datos

Libros

Cien Años de Soledad
Autor: Gabriel García Márquez
Fecha de Donación: 2022-03-15
Condición: Excelente
Nombre del Donante: María Fernández
Don Quijote de la Mancha

Autor: Miguel de Cervantes
Fecha de Donación: 2021-06-20
Condición: Buena
Nombre del Donante: Juan Pérez
La Sombra del Viento

Autor: Carlos Ruiz Zafón
Fecha de Donación: 2023-01-10
Condición: Regular
Nombre del Donante: Luis González


