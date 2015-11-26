
import pprint

from django.http import HttpResponse
from django.views.generic import TemplateView

from .models import ServiceTemplate

pp = pprint.PrettyPrinter(indent=4)


class RenderTemplateView(TemplateView):

    """
    Just render template
    """

    template_name = 'base.html'

    def get(self, request, *args, **kwargs):

        template = ServiceTemplate.objects.get(pk=self.kwargs.get('pk'))

        return HttpResponse(
            pprint.pformat(template.get_yaml_content()),
            content_type="application/json")
