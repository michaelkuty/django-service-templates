from jinja2 import Environment
from dbtemplates.models import Template


class JinjaRenderer(object):

    '''Object for rendering'''

    env = Environment()

    def render(self, name=None, template=None, context={}):
        ''''Render Template meta from jinja2 templates.

        '''

        if isinstance(template, Template):
            _template = template
        else:
            _template = Template.objects.get(name=name)

        # Maybe cache or save local ?
        response = self.env.from_string(
            _template.content).render(context)

        return response

renderer = JinjaRenderer()
