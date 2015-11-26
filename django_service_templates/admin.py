
from django.contrib import admin

from .models import ServiceTemplate


class ServiceTemplateAdmin(admin.ModelAdmin):
    # this breaks yaml output now
    #readonly_fields = ("rendered",)
    change_form_template = 'admin/change_form_with_render_button.html'

admin.site.register(ServiceTemplate, ServiceTemplateAdmin)
