from django.http import HttpResponse
from django.views.generic import TemplateView


def helloFunc(req):
    return HttpResponse("hello world")


class HelloWorldClass(TemplateView):
    template_name = "hello.html"
