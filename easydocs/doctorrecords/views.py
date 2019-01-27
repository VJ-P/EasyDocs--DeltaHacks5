# Imports
from django.shortcuts import render

import datetime
from . import db_models as db
from docx import Document
from docx.shared import Inches
from docx.shared import Pt
import os


def docCreate(appointment, time, filename):
    patient = appointment.patient
    PCF = Document()
    
    age = (time.date() - patient.date_of_birth).days/365
    
    #set styles
    style = PCF.styles['Title']
    font1 = style.font
    font1.name = 'Arial'
    font1.size = Pt(30)

    style = PCF.styles['Heading 1']
    font2 = style.font
    font2.name = 'Arial'
    font2.size = Pt(18)
    font2.bold = False

    style = PCF.styles['Heading 2']
    font3 = style.font
    font3.name = 'Arial'
    font3.size = Pt(16)
    font3.bold = False

    style = PCF.styles['Normal']
    font4 = style.font
    font4.name = 'Arial'
    font4.size = Pt(12)

    #margins
    section = PCF.sections[0]
    section.left_margin = Inches(0.5)
    section.right_margin = Inches(0.5)
    section.top_margin = Inches(0.5)
    section.bottom_margin = Inches(0.5)

    #header
    PCF.add_heading('Patient Consultation Form', 0)

    p1 = PCF.add_paragraph('')
    p1.add_run('Healthcare Practitioner: ').bold = True
    p1.add_run("\t\tDr. Melvin Hobbs")
    p1.style = PCF.styles['Normal']

    p = PCF.add_paragraph('')
    p.add_run('Date: \t\t\t\t\t').bold = True
    p.add_run(time.strftime("%Y-%m-%d"))

    PCF.add_heading('Patient Information', 1)
    PCF.add_paragraph('Name: \t\t' + str(patient.full_name()))
    PCF.add_paragraph('Gender: \t\t' + patient.sex)

    PCF.add_paragraph('Date of Birth: \t' + patient.date_of_birth.strftime("%Y-%m-%d") + '\t\t\t Age:\t' + str(age))
    PCF.add_paragraph('Address: \t\t' + str(patient.full_address()))

    PCF.add_paragraph('Phone: \t\t' + patient.phone_number)
    PCF.add_paragraph('HCN: \t\t\t' + patient.healthcard_number)

    PCF.add_heading('Family History', 1)
    for fam in patient.family_history.all():
        PCF.add_paragraph(fam.family_member)
        for condition in fam.condition.all():
            PCF.add_paragraph(condition.name, style='List Bullet')
    p = PCF.add_paragraph('')
    p.add_run('Notes: ').bold = True

    PCF.add_heading('Ongoing Conditions', 1)
    for OC in patient.active_conditions.all():
        PCF.add_heading(OC.condition.name, 2)
        PCF.add_paragraph('Diagnosed:\t\t\t\t\t\t' + OC.diagnosis_date.strftime("%Y-%m-%d"))
        PCF.add_paragraph('Method of Treatment:\t\t\t' + OC.get_treatment().name)
        PCF.add_paragraph('Started:\t\t\t\t\t\t\t' + OC.treatment_start_date.strftime("%Y-%m-%d"))
        PCF.add_paragraph('Perscription Ends:\t\t\t\t' + OC.treatment_renewal_date.strftime("%Y-%m-%d"))
        PCF.add_heading("Possible Side Effects")
        for SE in OC.condition.side_effects.all():
            PCF.add_paragraph(SE.effect, style='List Bullet')
        PCF.add_paragraph("Side Effects Noticed\tYes\tNo")
        p = PCF.add_paragraph("Recently Discovered Treatments:\t")
        for NT in OC.condition.new_treatments().all():    
            p.add_run(NT.name + ", ").italic = True
        #PCF.add_paragraph("Incompatible Treatments:\t\t\t" + )
        p = PCF.add_paragraph('')
        p.add_run('Notes: ').bold = True

    PCF.add_heading('Potential Risks', 1)
    #   run a loop for each condition
    #   PCF.add_paragraph("Alzeimer's:")
    #   p1 = PCF.add_paragraph('\tAge, gender')

    PCF.add_heading('Additional Notes: ', 1)

    path_relative='export_docs' + ('\\' if os.name == 'nt' else '/') + filename + '.docx'
    path = os.path.join(os.path.dirname(__file__), path_relative)
    
    #create the form
    PCF.save(path)






















# Create your views here.s
def homepage(request):
    hcpList = db.HealthcareProviders.objects.all()

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
                    apt = db.Appointments.objects.filter(pk=apt_id)[0]
                    docCreate(apt, now, apt.patient.first_name)

        if (hcp_id != -1):
            hcp_selected = db.HealthcareProviders.objects.get(pk=hcp_id)

            if date_start and date_end: 
                appointment_list = db.Appointments.objects.filter(healthcare_provider=hcp_selected).filter(date__range=[date_start_str, date_end_str]).order_by('date')
        
    
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


#def download(request, filename):
    