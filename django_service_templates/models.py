from __future__ import unicode_literals

from datetime import datetime

import yaml
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from polymorphic import PolymorphicModel
from yamlfield.fields import YAMLField

from .engine import renderer
from .signals import render_template


@python_2_unicode_compatible
class ServiceTemplate(PolymorphicModel):

    '''Base object with have template and context
    then could be rendered or tranformed
    '''

    label = models.CharField(verbose_name=_(
        'Label'), max_length=250, null=True, blank=True)

    path = models.CharField(
        verbose_name=_('Path pattern'), max_length=250, null=True, blank=True,
        help_text=_('Somethink like this: srv/salt/leonardo/app/{name}.yml'))

    template = models.ForeignKey(
        'dbtemplates.Template',
        verbose_name=_("Template"),
        related_name="service_templates",
        blank=True, null=True)

    context = YAMLField(blank=True, null=True)
    extra = YAMLField(blank=True, null=True)

    modified = models.DateTimeField(blank=True, null=True)
    rendered = models.TextField(blank=True, null=True)
    sync = models.NullBooleanField(help_text=_('Keep synced with Salt Master'))

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("User"),
        related_name="service_templates",
        help_text=_('Optionaly assign to user'),
        null=True, blank=True)

    def __str__(self):
        return self.label

    @property
    def content(self):
        '''returns rendered content'''

        if self.rendered:
            return self.rendered

        self.rendered = self.render()
        self.save()

        return self.rendered

    @property
    def yaml_content(self):
        '''specific reclass/heat method'''
        try:
            yaml_content = yaml.load(self.content)
        except:
            pass
        else:
            return yaml_content
        return dict()

    def get_yaml_content(self):
        '''Obsolete use yaml_content property'''
        return self.yaml_content

    def get_content(self):
        '''Obsolete use content property'''
        return self.content

    def render(self, context={}):
        '''Render Template with context'''

        meta = renderer.render(
            template=self.template,
            context=self.get_context(context))

        return meta

    def get_path(self, context={}):
        '''Render Context to path variable and return it'''
        return self.path.format(**self.get_context(context))

    def get_context(self, extra_context={}):
        '''return updated context where extra is primary'''
        ctx = self.context or {}
        ctx.update(extra_context)
        return ctx

    def save(self, *args, **kwargs):

        if self.sync:
            # render with fail silently
            try:
                self.rendered = self.render()
                self.modified = datetime.now()
            except Exception as e:
                if settings.DEBUG:
                    raise e

        super(ServiceTemplate, self).save(*args, **kwargs)

        if self.sync:
            render_template.send(sender=self.__class__, template=self)

    class Meta:
        verbose_name = _("Serviec Template")
        verbose_name_plural = _("Service Templates")
