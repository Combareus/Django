from django.shortcuts import render
from django.http import HttpResponse
from schedule.models import Surgeon

def home(request):
    '''
    Displays homepage
    '''
    return render(request, 'home.html')
# Create your views here.
