# Imports
from django.shortcuts import render

import datetime


# Create your views here.
def homepage(request):

    now = datetime.datetime.now()


    return render(request, 'home.html',
    {
        'todayYYYYMMDD':          now.strftime("%Y-%m-%d"),
        'todayWeekday':         now.strftime("%A"),               
    })
