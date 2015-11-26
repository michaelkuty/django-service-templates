
========================
django-service-templates
========================

Manage your service templates via Django Admin.

.. contents::
    :local:

Installation
------------

.. code-block:: bash

    pip install django-service-templates

Usage
-----

.. code-block:: bash

	from dbtemplates import Template
    from django_service_templates.models import ServiceTemplate

    class HeatTemplate(ServiceTemplate):

        # your awesome stuff

        pass

	dbtemplate = Template.objects.create(name='My Jinja2 Template', content='{{ name }}')

    HeatTemplate.objects.create(template=dbtemplate, context={'name': 'My name'}).render()

    > 'My name'