#this line doesn't work but its default so ill keep it here ig
#from django.test import TestCase

#imports 
from classes import Surgeon, Employee, Patient, Schedule, Cleaner

# Create your tests here.

from datetime import datetime, timedelta
#this is a TEXT BASED test
surgeon1 = Surgeon("John Doe", "Sr")
print(str(surgeon1))
time = datetime.now() - timedelta(hours = 11)
print(time)
