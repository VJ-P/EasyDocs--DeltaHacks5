# Imports
from django.shortcuts import render

import datetime
from . import models


# Create your views here.s
def homepage(request):
    hcpList = models.HCP.objects.all()
    now = datetime.datetime.now()

    if request.POST:
        selectedHCP = models.HCP.objects.get(pk=request.POST.get('dds_HealthcareProviders'))
        appointmentList = models.Appointment.objects.filter(doctor=selectedHCP)
    else:
        selectedHCP = None
        appointmentList = None
    


    
    return render(request, 'home.html',
    {
        'todayYYYYMMDD':            now.strftime("%Y-%m-%d"),
        'todayWeekday':             now.strftime("%A"),
        'HealthcareProviders':      hcpList,
        'SelectedHCP':              selectedHCP,
        'Appointments':             appointmentList,
        'StartDate':                now,
        'EndDate':                  now
    })
