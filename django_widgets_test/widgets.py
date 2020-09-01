import os
import django_widgets


class HelloWidget(django_widgets.Widget):
    root = os.path.dirname(__file__) + '/templates'
    template_name = 'django_widgets_test/widgets/hello.html'
    # path to template

    class Media:
        extend = False
        script = {
            'text/javascript': {
                'script-hello': ('django_widgets_test/widgets/hello.js', 'django_widgets_test/widgets/hello2.js')
            }
        }
        style = {
            'all': ('django_widgets_test/widgets/hello.css', 'django_widgets_test/widgets/hello.span.css')
        }


class HelloJinja2Widget(HelloWidget):
    template_name = 'django_widgets_test/widgets/hello.jinja2'
