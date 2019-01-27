# Imports
from django.shortcuts import render

import datetime
from . import models


# Create your views here.
def homepage(request):
    hcpList = models.HCP.objects.all()
    now = datetime.datetime.now()

    if request.method == 'POST':
        answer = request.POST['dds_HCP']
    else:
        answer = "none"

    if(request.GET.get('btn_searchHCP')):
        hcp = request.GET.get('textbox_HCP')
    else:
        hcp = "Not found..."

    
    return render(request, 'home.html',
    {
        'todayYYYYMMDD':            now.strftime("%Y-%m-%d"),
        'todayWeekday':             now.strftime("%A"),
        'hcpList':                  hcpList,
        'ans':                      answer
    })
