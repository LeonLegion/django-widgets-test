from django_widgets.api import add_widget
from django.views.generic import TemplateView
from .widgets import HelloWidget


class IndexView(TemplateView):
    template_name = 'django_widgets_test/index.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        add_widget(request, 'hello', HelloWidget())

