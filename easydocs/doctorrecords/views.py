# Imports
from django.shortcuts import render

import datetime

# Create your views here.
def homepage(request):
    return render(request, 'home.html')


# Variables
now = datetime.datetime.now()



# Accessors - General
def _todayYYYMMDD():
    return now.strftime("%Y-%m-%d")

def _todayWeekday():
    return now.strftime("%A")



# Accessors - Patient
def _patientName():
    return "Alex Jones"

def _patientSex():
    return "Male"

def _patientDOB():
    return "1995-04-20"

def _patientAddress():
    return "1234 Boulevard Street, Hamilton, ON, Canada"

def _patientPhone():
    return "+1 (431) 555-22398"

def _patientHCN():
    return "9876 - 9987 - 233 - WP"
    