# Imports
from django.shortcuts import render

import datetime
from . import models


# Create your views here.s
def homepage(request):
    hcpList = models.HCP.objects.all()
    now = datetime.datetime.now()

    if request.POST:
        selectedHCP = models.HCP.objects.get(pk=request.POST.get('dds_HCPs'))
    else:
        selectedHCP = hcpList[0]


    if(request.GET.get('btn_searchHCP')):
        hcp = request.GET.get('textbox_HCP')
    else:
        hcp = "Not found..."

    
    return render(request, 'home.html',
    {
        'todayYYYYMMDD':            now.strftime("%Y-%m-%d"),
        'todayWeekday':             now.strftime("%A"),
        'hcpList':                  hcpList,
        'selectedHCP':                   selectedHCP
    })
