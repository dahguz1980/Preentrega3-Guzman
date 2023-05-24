# Preentrega3-Guzman - CODERHOUSE

Aplicación que permite gestionar las calificaciones de los estudiantes. 

## CONSIDERACIONES IMPORTANTES

El sistema permite agregar, Estudiante, Profesor, Matería y Notas. 

- Para agregar Matería tiene que existir al menos un Profesor

- Para Agregar Notas, debe exitir Materias y Alumnos en la base de datos

## CONFIGURACIÓN

1. Clonar el Repositorio

> `git clone https://github.com/dahguz1980/Preentrega3-Guzman.git`

2. Abre el Visual Studio Code y Abre la Carpeta ***Preentrega3-Guzman***

3. Abre el Archivo requirements.txt y presiona el botón "crear entorno".

> Una vez ejecutado se debe crear el entorno virtual .venv 

4. Activar el entorno virtual

> En Windows ejecuta `.\venv\Scripts\activate`

> En Mac o Linux ejecuta `source .venv/bin/activate`

5. Abre el terminal en VSC, verifica que el entorno virtual está activo (.venv) 

> Ejecuta `pip list` y verifica que todas las dependencias están instaladas

6. Ingresa en la carpeta project y ejecuta lo siguiente

    ***En Mac cambiar python por python3***

>`python manage.py makemigrations`

>`python manage.py migrate`

7. Por último ejecutar, para ver los archivos statics con el Debug False

> `py manage.py collectstatic`

## BASE DE DATOS

Base de datos de 4 tablas 

![Database Model!](project/apps/GradeApp/static/GradeApp/assets/database.png "Grade App Database")


