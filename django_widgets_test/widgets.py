import os
import django_widgets


class HelloWidget(django_widgets.Widget):
    root = os.path.dirname(__file__) + '/templates'
    template_name = 'django_widgets_test/widgets/hello/hello.html'
    # path to template

    class Media:
        extend = False
        script = {
            'text/javascript': {
                'script-hello': ('django_widgets_test/widgets/hello/hello.js', 'django_widgets_test/widgets/hello/hello.log.js')
            }
        }
        style = {
            'all': ('django_widgets_test/widgets/hello/hello.css', 'django_widgets_test/widgets/hello/hello.span.css')
        }


class HelloJinja2Widget(HelloWidget):
    template_name = 'django_widgets_test/widgets/hello/hello.jinja2'
