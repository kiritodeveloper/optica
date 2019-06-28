# Sistema de mediciones para la Optica Latyna
## Instalación
### Requerimientos
* Python 2.7
### Procedimiento
1. Instalar los paquetes necesarios para que la aplicación funcione usando el comando:
> pip install -r requirements.txt

**Nota:** *Si se va a instalar en un sistema operativo windows, la libreria Msqldb requiere que primero instale VCForPython27, descárguelo desde acá: http://aka.ms/vcpython27*

**Información:** *Si tiene problemas para instalar la librería MySQL_python, utilise el archivo *MySQL_python-1.2.5-cp27-none-win32.whl* ubicado dentro de la carpeta adicionales/Mysqldb corriendo el comando*
> pip install MySQL_python-1.2.5-cp27-none-win32.whl
2. Revisar la configuración de la base de datos dentro del archivo *optica/settings.py*
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'latyna',
        'USER': 'root',
        'PASSWORD': '0ptic4',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```
3. Crear la base de datos usando los comandos
> python  manage.py migrate auth

> python manage.py migrate
4. Crear una cuenta se super usuario con el comando. Se recomienda usar estos valores por defecto:
> python manage.py createsuperuser
* username: administrator
* email: admin@latyna.com
* password: 0pt1c4
5. Correr el siguiente comando para recolectar todos los archivos estaticos requeridos
> python manage.py collectstatic
6. Para hechar a andar el sistema, use el comando
> python manage.py runserver \<ip:port>

## Deploy application using apache and mod_wsgi
1. Considerar que se utilizará una versión de mod_wsgi de 32 bits, por lo que la versión de python también debe ser de 32 bits.
2. Instalar xampp usando en instalador _xampp-win32-1.8.2-6-VC9-installer_, lo puede desvargar de https://sourceforge.net/projects/xampp/files/XAMPP%20Windows/1.8.2/xampp-win32-1.8.2-6-VC9-installer.exe/download
3. Instalar virtualenv usando el comando
> pip  install virtualenv
4. Crear un entorno virtual para instalar los paquetes requeridos de python para el funcionamiento del sistema. Para esta guia, crearemos el entorno virtual dentro de la carpeta del proyecto con nombre *opticaenv*, para esto usamos el comando
> virtualenv opticaenv
5. Instalar todas las dependencias del sistema con el comando
> pip install -r requirements.txt
6. Instalar el mod_wsgi, usando el paguete .whl ubicado en la carpeta D:\Proyectos\Django\optica\adicionales\mod_wsgi del proyecto, usamos el comando
> pip install mod_wsgi-4.5.24+ap24vc9-cp27-cp27m-win32.whl
7. Cambiamos la configuración del archivo en optica.wsgi.py a la siguiente configuración:
```python
import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('D:/Proyectos/Django/optica/opticaenv/Lib/site-packages')
# Add the app's directory to the PYTHONPATH
sys.path.append('D:/Proyectos/Django/optica')
os.environ['DJANGO_SETTINGS_MODULE'] = 'optica.settings'
# Activate your virtual env
activate_env=os.path.expanduser("D:/Proyectos/Django/optica/opticaenv/Scripts/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
``` 
8. En el archivo http.conf de nuestro servidor apache, añadimos las siguientes lineas la final del archivo:
```
LoadModule wsgi_module "D:/Proyectos/Django/optica/opticaenv/Lib/site-packages/mod_wsgi/server/mod_wsgi.pyd"
WSGIScriptAlias / "D:/Proyectos/Django/optica/optica/wsgi.py"  
WSGIPythonPath "D:/Proyectos/Django/optica:D:/Proyectos/Django/optica/opticaenv/Lib/site-packages"  
<Directory "D:/Proyectos/Django/optica/optica">  
  <Files wsgi.py>  
       Require all granted  
  </Files>  
</Directory>  
Alias /media/ D:/Proyectos/Django/optica/media/  
Alias /static/ D:/Proyectos/Django/optica/static/  
<Directory D:/Proyectos/Django/optica/static>  
  Require all granted  
</Directory>  
<Directory D:/Proyectos/Django/optica/media>  
  Require all granted  
</Directory>  

```

8. pagina referencial web componentes :
> pip install componet https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysql-python
> pip install componet https://www.lfd.uci.edu/~gohlke/pythonlibs/#mod_wsgi
