from django.apps import AppConfig
from django.conf import settings
import os


class UsersConfig(AppConfig):
    #default_auto_field = 'django.db.models.BigAutoField'
    #name = os.path.join(settings.BASE_DIR, 'users')
    name = 'users'
    path = os.path.join(settings.BASE_DIR, 'users')
    #path = './users'
    def ready(self):
        import users.signals
