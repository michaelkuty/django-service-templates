from django.dispatch import Signal

render_template = Signal(providing_args=["template"])
template_rendered = Signal(providing_args=["template"])
