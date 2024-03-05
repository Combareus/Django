"""
Functions to be used in main (a lot of logic)
Creation - 02/28
"""

#imports 
from models import Surgeon
#from models import Employee
from models import Patient
from models import Schedule
from models import Cleaner

def add_surgeon(surgeons, name, exp):
    """
    Function for adding a surgeon to surgeons
    """
    surgeons.append(Surgeon(name, exp))

def edit_surgeon(surgeons, name, newexp, newavailability, newqualifications):
    """
    Function for changing a surgeon's info
    Return 
    True - Surgeon found and changed
    False - Surgeon not found
    """
    for x in surgeons:
        if x.name == name:
            x.exp = newexp
            x.availability = newavailability
            x.qualifications = newqualifications
            #surgeon found and edited
            return True
    #surgeon not found
    return False

def add_patients(patients, name, conditionType, severity):
    """
    Function for adding a patient to patients
    """
    patients.append(Patient(name, conditionType, severity))

def edit_patient(patients, name, newconditionType, newseverity):
    """
    Function for changing a patient's info
    Return 
    True - patient found and changed
    False - patient not found
    """
    for x in patients:
        if x.name == name:
            x.conditionType = newconditionType
            x.severity = newseverity
            #patient found and edited
            return True
    #patient not found
    return False

def add_cleaner(cleaners, name):
    """
    Function for adding a cleaner to cleaners
    """
    cleaners.append(Cleaner(name))

def edit_cleaner(cleaners, name, newavailability):
    """
    Function for changing a cleaner's info
    Return 
    True - cleaner found and changed
    False - cleaner not found
    """
    for x in cleaners:
        if x.name == name:
            x.availability = newavailability
            #cleaner found and edited
            return True
    #cleaner not found
    return False

def compare_date(time1, time2):
    """
    Compares two dates and returns the earliest one
    If there is a tie, return first time given
    Time1 - (list of ints) [MM, DD, YYYY]
    Time2 - (list of ints) [MM, DD, YYYY]
    """
    if time1[2] < time2[2]:
        return time1
    elif time1[2] > time2[2]:
        return time2
    elif time1[1] < time2[1]:
        return time1
    elif time1[1] > time2[1]:
        return time2
    elif time1[0] < time2[0]:
        return time1
    elif time1[0] > time2[0]:
        return time2
    return time1

#def schedule_surgery(surgeons, cleaners, patients, time):
