# Proyecto Django Tercera Pre entrega Peña Rafael

## Requisitos
- Python 3.x
- Django

## Instalación
1. Clonar el repositorio:
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd Tercerpapre-entrega+PenaRafael
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

3. Ejecutar el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```

4. Acceder a la aplicación en el navegador:
    - **Crear un nuevo libro:** [http://127.0.0.1:8000/biblioteca/crear_libro/](http://127.0.0.1:8000/biblioteca/crear_libro/)
    - **Buscar libros:** [http://127.0.0.1:8000/biblioteca/buscar/](http://127.0.0.1:8000/biblioteca/buscar/)
    - **Interfaz de administrador:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Funcionalidades
- Formulario para agregar un libro al catalogode donaciones.
- Búsqueda de libros por título.
- Interfaz de administrador para gestionar autores, libros y editoriales.

## Datos de Ejemplo para Búsqueda
### Set 1
- **Título:** Cien Años de Soledad
- **Autor:** Gabriel García Márquez
- **Fecha de Donación:** 2022-03-15
- **Condición:** Excelente
- **Nombre del Donante:** María Fernández

### Set 2
- **Título:** Don Quijote de la Mancha
- **Autor:** Miguel de Cervantes
- **Fecha de Donación:** 2021-06-20
- **Condición:** Buena
- **Nombre del Donante:** Juan Pérez

### Set 3
- **Título:** La Sombra del Viento
- **Autor:** Carlos Ruiz Zafón
- **Fecha de Donación:** 2023-01-10
- **Condición:** Regular
- **Nombre del Donante:** Luis González


## Estructura del Proyecto
- `biblioteca/models.py`: Definición de los modelos `Autor`, `Libro` y `Editorial`.
- `biblioteca/formularios.py`: Formularios para los modelos.
- `biblioteca/views.py`: Vistas para manejar la lógica de los formularios y las búsquedas.
- `biblioteca/plantillas/vistas/`: Plantillas HTML con diseño y herencia.
- `biblioteca/static/biblioteca/styles.css`: Archivo CSS para el diseño de las plantillas.


