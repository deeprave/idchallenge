from envex import env

from django.core.wsgi import get_wsgi_application

env.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
