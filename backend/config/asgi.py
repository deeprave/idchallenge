from envex import env
from django.core.asgi import get_asgi_application

env.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_asgi_application()
