import os
import django_widgets
from django.templatetags.static import static


class HelloWidget(django_widgets.Widget):
    template_name = 'django_widgets_test/widgets/hello/hello.html'
    # path to template

    class Media:
        extend = False
        script = {
            'text/javascript': {
                'script-hello': ('django_widgets_test/widgets/hello/hello.js', 'django_widgets_test/widgets/hello/hello.log.js'),
            },
        }
        style = {
            'all': ('django_widgets_test/widgets/hello/hello.css', 'django_widgets_test/widgets/hello/hello.span.css'),
            'print': ('django_widgets_test/widgets/hello/hello.print.css',),
        }


class HelloJinja2Widget(HelloWidget):
    template_name = 'django_widgets_test/widgets/hello/hello.jinja2'

    def get_context(self, name, data, attrs):
        context = super().get_context(name, data, attrs)
        context['name'] = 'Jinja2'
        return context

    class Media:
        extend = True
        script = {
            'text/x-template': {
                'hello-template': ('django_widgets_test/widgets/hello/hello.template',)
            }
        }
        js = {
            'async': (
                static('django_widgets_test/widgets/hello/greetings.js'),
            ),
        }
        css = {
            'all': (
                static('django_widgets_test/widgets/hello/hello.css'),
            ),
        }
