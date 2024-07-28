"""
WSGI config for Tercera_preentrega_penaRafael project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Tercera_preentrega_penaRafael.settings')

application = get_wsgi_application()
