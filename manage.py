#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "optica.settings")

    from django.core.management import execute_from_command_line
#    print(sys.argv[1])
 #   argv = ['manage.py','runserver']
    execute_from_command_line(sys.argv)
