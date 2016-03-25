from unittest import loader

from django.http import HttpResponse
from django.shortcuts import render_to_response, render

# Create your views here.
from django.template import Template,Context
from django.utils.timezone import now


def hello(request):
    time=now()
    template = Template("<html><body>My name is {{ time }}.</body></html>")
    context = Context({"time": time})
    m=template.render(context)
    return HttpResponse(m)