#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from sys import path as sys_path
from django.conf import settings

"""
def main():
    #Run administrative tasks.
    #os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'graduation_project.settings')
    #os.environ['DJANGO_SETTINGS_MODULE'] = 'graduation_project.settings'
    #import django
    #django.setup()

    #from django.core.management import call_command

    #import django
    #django.setup()
    #from django.core.management import call_command
    #sys_path.append('graduation_project.settings')    
    #environ.setdefault('DJANGO_SETTINGS_MODULE', 'graduation_project.settings')

    
    #django.setup()

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
"""

import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'graduation_project.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)