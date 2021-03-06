from django_widgets.api import add_widget
from django.views.generic import TemplateView
from .widgets import HelloWidget, HelloJinja2Widget


class IndexView(TemplateView):
    template_name = 'django_widgets_test/index.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        add_widget(request, 'hello', HelloWidget())


class Jinja2View(TemplateView):
    template_name = 'django_widgets_test/index.jinja2'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['world'] = 'World'
        return context

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        add_widget(request, 'hello', HelloJinja2Widget())
