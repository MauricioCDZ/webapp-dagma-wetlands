"""
WSGI config for graduation_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
#from users.apps import UsersConfig

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'graduation_project.settings')
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'graduation_project.settings')
application = get_wsgi_application()
#print("HOLAAAAAAAAA")
