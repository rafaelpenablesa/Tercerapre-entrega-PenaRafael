# Proyecto Django con Patrón MVT

## Requisitos
- Python 3.x
- Django

## Instalación
1. Crear un entorno virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
2. Instalar dependencias:
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

## Funcionalidades
- Formulario para crear un autor.
- Búsqueda de libros por título.

## Orden de Pruebas
1. Acceder a `/biblioteca/crear_autor/` para crear un nuevo autor.
2. Acceder a `/biblioteca/buscar/` para buscar libros en la base de datos.

