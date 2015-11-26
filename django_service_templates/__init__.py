
from django.apps import AppConfig

default_app_config = 'django_service_templates.Config'


LEONARDO_APPS = ['django_service_templates', 'dbtemplates']


class Config(AppConfig):
    name = 'django_service_templates'
    verbose_name = "django-service-templates"
