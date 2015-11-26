
from django.contrib import admin

from .models import ServiceTemplate


class ServiceTemplateAdmin(admin.ModelAdmin):
    # this breaks yaml output now
    #readonly_fields = ("rendered",)
    pass

admin.site.register(ServiceTemplate, ServiceTemplateAdmin)
