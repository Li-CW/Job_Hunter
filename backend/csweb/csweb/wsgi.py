"""
WSGI config for csweb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

profile = os.environ.get("PROJECT_PROFILE", "develop")
print(profile)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "csweb.settings.%s" % profile)

application = get_wsgi_application()
