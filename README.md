# Proyecto Django con Patrón MVT

## Requisitos
- Python 3.x
- Django

## Instalación
1. Clonar el repositorio:
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd Tercera_preentrega_penaRafael
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

3. Acceder a la aplicación en el navegador:
    - Crear un nuevo autor: [http://127.0.0.1:8000/biblioteca/crear_autor/](http://127.0.0.1:8000/biblioteca/crear_autor/)
    - Buscar libros: [http://127.0.0.1:8000/biblioteca/buscar/](http://127.0.0.1:8000/biblioteca/buscar/)

## Funcionalidades
- Formulario para crear un autor.
- Búsqueda de libros por título.

## Estructura del Proyecto
- `biblioteca/models.py`: Definición de los modelos `Autor`, `Libro` y `Editorial`.
- `biblioteca/formularios.py`: Formularios para los modelos.
- `biblioteca/views.py`: Vistas para manejar la lógica de los formularios y las búsquedas.
- `biblioteca/plantillas/vistas/`: Plantillas HTML con diseño y herencia.
- `biblioteca/static/biblioteca/styles.css`: Archivo CSS para el diseño de las plantillas.
