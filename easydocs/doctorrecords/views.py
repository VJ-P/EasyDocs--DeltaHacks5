# Imports
from django.shortcuts import render

import datetime
from . import db_models as db
from . import doccreator as dc

# Create your views here.s
def homepage(request):
    hcpList = db.HCP.objects.all()

    dt = datetime.datetime
    now = dt.now()

    hcp_selected = None
    appointment_list = None

    date_start_str = request.POST.get('date_Start')
    date_end_str   = request.POST.get('date_End')

    date_start = dt.strptime(date_start_str, '%Y-%m-%d') if date_start_str else None
    date_end = dt.strptime(date_end_str, '%Y-%m-%d') if date_end_str else None

    if request.POST:

        if date_start and date_end and date_end < date_start:
            date_end = date_start

        if request.POST.get("btn_Today"):
            date_start = now
            date_end = now
            date_start_str = now.strftime("%Y-%m-%d")
            date_end_str = now.strftime("%Y-%m-%d")

        hcp_id = (int) (request.POST.get('dds_HealthcareProviders'))

        appointment_gen_list = request.POST.getlist('appointments')

        if request.POST.get("generate"):
            for apt_id in appointment_gen_list:
                if apt_id:
                    apt = db.Appointment.objects.filter(pk=apt_id)[0]
                    print(apt)
                    dc.docCreate(apt.patient, now, apt.patient.first_name)

        if (hcp_id != -1):
            hcp_selected = db.HCP.objects.get(pk=hcp_id)

            if date_start and date_end: 
                appointment_list = db.Appointment.objects.filter(doctor=hcp_selected).filter(date__range=[date_start_str, date_end_str]).order_by('date')
        
    
    return render(request, 'home.html',
    {
        'todayYYYYMMDD':            now.strftime("%Y-%m-%d"),
        'todayWeekday':             now.strftime("%A"),
        'HealthcareProviders':      hcpList,
        'SelectedHCP':              hcp_selected,
        'Appointments':             appointment_list,
        'StartDate':                date_start,
        'EndDate':                  date_end
    })
