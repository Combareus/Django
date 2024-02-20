from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# view function: request -> response (request handler)


def say_hello(request):
    '''
    Testing View Function that is called at an url

    '''
    return HttpResponse("Hello world:)")
