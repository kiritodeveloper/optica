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

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "optica.settings")

application = get_wsgi_application()
