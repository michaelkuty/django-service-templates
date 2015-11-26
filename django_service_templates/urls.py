
from django.conf.urls import url

from .views import RenderTemplateView

urlpatterns = [
    url(r'^(?P<pk>.*)/render$', RenderTemplateView.as_view(), {}, 'render_template'),
]
