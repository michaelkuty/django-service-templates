# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_service_templates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicetemplate',
            name='template',
            field=models.ForeignKey(related_name='service_templates', verbose_name='Template', blank=True, to='dbtemplates.Template', null=True),
        ),
    ]
