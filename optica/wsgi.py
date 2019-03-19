"""
WSGI config for optica project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

# Development configuration

# import os
#
# from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "optica.settings")
#
# application = get_wsgi_application()

# Production configuration

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