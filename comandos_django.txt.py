"""
	Fecha_Creacion:	2022-10-06
	Descripcion		:	Este archivo contiene los comandos mas usados por mi en el curso de Django
	URL Curso 		:	https://www.udemy.com/course/master-en-python-aprender-python-django-flask-y-tkinter/learn/lecture/19223550#overview
	OS						:	Windows 11
	Autor					:	Daniel Torres Martinez
	github				:	
	
"""
# Instalar Python
	
	#	Descargando De Pagina Oficial
	https://www.python.org/downloads/
	https://www.python.org/ftp/python/3.10.7/python-3.10.7-amd64.exe
	
# Instalar Visual Studio Code
	
	#	Descargar De Pagina Oficial
	https://code.visualstudio.com/download#
	https://az764295.vo.msecnd.net/stable/64bbfbf67ada9953918d72e1df2f4d8e537d340e/VSCodeSetup-x64-1.72.0.exe
		
# Instalar DJango
	# Abrimos Terminal y Ejecutamos
	pip install Django==3.0.5  #	Indicamos la version 3.0.5
	
	# Comprobar version instalada de DJango
	python -m django --version
	
# Crear primer poyecto de DJango
	# Ubicarnos en la carpeta donde queremos crear el proyecto
	
	comando: django-admin
	parametro: startproject
	nombre del proyecto: AprendiendoDjango # El nombre no puede contener caractgeres especiales, no guiones, no espacios
	
	# Ejecutamos
	django-admin startproject AprendiendoDjango  # Si no sale ningun mensaje es porque el proyecto se creo con Exito.
	
	#	Se crea un directorio con la estructura de un proyecto Django
	
	#	Ingresamos al Directorio con ChangeDirectory
	cd AprendiendoDjango  # En esta se encuentra otro directorio llamado igual al projecto y un archivo "manage.py"
	
	#	Arrancamos nuestra aplicacion Web	ejecutamos el comando "migrate" desde el archivo "manage.py"
	python manage.py migrate 	#Esto crea una base de  Datos en SQLite3 e inicializa las configuracion del projecto
	
	#	Inicializamos el servidor 
	python manage.py runserver  
	
	# Debemos ingresar al navegador y pegar esta URL
	http://127.0.0.1:8000/
		
	#	Abrimos con VS Code
	code .
	

# Crear APP: estas secrean por cada modulo, funcionalidad o entidad que tengamos en el projecto
#	Estas se configuran en el archivo "settings.py" en la seccion INSTALLED_APPS = []

	#	crear una app dento de mi projecto, me ubico dentro del proyecto
	cd AprendiendoDjango
	
	python manage.py startapp miapp #	el comando "startapp" crea la app, y "miApp" es el nombre o modulo que quiero crear
	
	#	Trabajando con vistas
	MVC = Modelo, Vista, Controlador-> El controlador tiene Acciones (metodos)
	MVT = Modelo, Template, Vista-> El controlador es llamdo Vista y tiene Acciones (metodos)
	

