#this line doesn't work but its default so ill keep it here ig
#from django.test import TestCase

#imports 
from models import Surgeon, Employee, Patient, Schedule, Cleaner

# Create your tests here.

from datetime import datetime, timedelta
#this is a TEXT BASED test

surgeon1 = Surgeon("John Doe", "Sr")
print(str(surgeon1))

cleaner1 = Cleaner("John Wayne")
print(str(cleaner1))

patient1 = Patient("John Wang", "Heart problems", 95)
print(str(patient1))

#adjusted to chinese time 
time = datetime.now() - timedelta(hours = 11)
print(time)

patient1.severity = 100
print(str(patient1))

