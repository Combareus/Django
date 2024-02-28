from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# view function: request -> response (request handler)


def say_hello(request):
    '''
    Testing View Function that is called at an url
    '''
    x=1
    y=2
    return render(request, 'hello.html', {'key': '1'})