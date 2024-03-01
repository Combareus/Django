from django.shortcuts import render
from django.http import HttpResponse
from schedule.classes import Surgeon, Employee, Patient, Schedule, Cleaner

# Create your views here.
# view function: request -> response (request handler)

def say_hello(request):
    '''
    Testing View Function that is called at an url
    '''
    x=1
    y=2
    return render(request, 'hello.html', {
        'key': '1', 
        })


def index(request):
    return render(request, 'index.html',{
        'Surgeons': [Surgeon("John Doe", "Sr"), Surgeon("Smith", "Sr")]
    })