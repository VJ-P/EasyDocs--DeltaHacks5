from django.db import models
import datetime
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
class SideEffects(models.Model):
    effect = models.CharField(max_length = 100, blank=True, null=True)

    def __str__(self):
        return self.effect

class Treatments(models.Model):
    name                    = models.CharField(max_length=30, blank=True, null=True)
    new                     = models.BooleanField(default=False)
    side_effects            = models.ManyToManyField(SideEffects, blank=True, null=True)

    def __str__(self):
        return str(self.name) if self.name else "HI"

    class Meta:
        verbose_name_plural = "Treatments"


class Conditions(models.Model):
    name                    = models.CharField(max_length=30, blank=True, null=True)
    treatments              = models.ManyToManyField(Treatments)
    side_effects            = models.ManyToManyField(SideEffects, blank=True, null=True)

    def __str__(self):
        return self.name

    def new_treatments(self):
        return self.treatments.all().filter(new=True)

    class Meta:
        verbose_name_plural = "Conditions"



class FamilyHistory(models.Model):
  FAMILY_MEMBER_CHOICES = (
    ('Father', 'Father'),
    ('Mother', 'Mother'),
    ('Grandfather', 'Grandfather'),
    ('Grandmother', 'Grandmother'),
    ('Sibling', 'Sibling')
  )
  family_member = models.CharField(choices=FAMILY_MEMBER_CHOICES, max_length=100)
  condition = models.ManyToManyField(Conditions)


class ActiveConditions(models.Model):
    diagnosis_date          = models.DateField(blank=True, null=True)
    treatment_start_date    = models.DateField(blank=True, null=True)
    treatment_renewal_date  = models.DateField(blank=True, null=True)
    condition               = models.ForeignKey(Conditions, on_delete=models.CASCADE)
    treatment               = models.ManyToManyField(Treatments, blank=True, null=True)

    def __str__(self):
        return str(self.condition.name)

    def get_treatment(self):
        return self.treatment.first()

    class Meta:
        verbose_name_plural = "Active Conditions"



class Incompatibilities(models.Model):
    treatment             = models.ForeignKey(Treatments, on_delete=models.CASCADE, related_name="treatment_queried")
    incompat_treatments   = models.ForeignKey(Treatments, on_delete=models.CASCADE, related_name="treatment_compared_to")
    incompat_conditions   = models.ForeignKey(Conditions, on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural = "Incompatabilities"

    def __str__(self):
        return str(self.treatment)

class Patient(models.Model):

    GENDER_CHOICES = (
        ('M', "Male"),
        ('F', 'Female')
    )

    first_name          = models.CharField(max_length=30, blank=True, null=True)
    last_name           = models.CharField(max_length=30, blank=True, null=True)
    sex                 = models.CharField(choices=GENDER_CHOICES, max_length = 6, blank=True, null=True)
    phone_number        = models.CharField(max_length=10, blank=True, null=True)
    healthcard_number   = models.CharField(max_length=12, blank=True, null=True)
    medication          = models.ManyToManyField(Treatments, blank = True, null=True)
    address             = models.CharField(max_length=100, blank=True, null=True)
    city                = models.CharField(max_length = 100, blank=True, null=True)
    province            = models.CharField(max_length = 100, blank=True, null=True)
    country             = models.CharField(max_length = 100, blank=True, null=True)
    postal_code         = models.CharField(max_length = 6, blank=True, null=True)
    date_of_birth       = models.DateField(blank=True, null=True)
    family_history      = models.ManyToManyField(FamilyHistory)
    active_conditions   = models.ManyToManyField(ActiveConditions)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def full_name(self):
        return self.first_name + " " + self.last_name

    def full_address(self):
        return  str(self.address) + ", " + str(self.city) + ", " + str(self.province) + ", " + str(self.country) + ", " + str(self.postal_code)
    
<<<<<<< Updated upstream
=======
    #DOES NOT WORK. I WILL FIX IT.
    """
    def get_conflicting_meds(patient):
      curr_treatments = patient.treatments
      incompat_treatments = Incompatabilities.objects.all()
      conflicting_med_lst = []
      for treatment in curr_treatments:
        for incompat in incompat_treatments:
          if treatment in incompat:
            conflicting_med_lst.add(treatment)
      return conflicting_med_lst
     """
>>>>>>> Stashed changes
    def get_patient_age(self):
        today = datetime.date.today()
        dob = Patient.date_of_birth()
        
        return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    
    def is_patient_at_risk(self):

        lst = []
        
        active_condition = str(self.active_conditions).lower()
        if patient_age > 65 and "diabetes" in active_condition:
            lst.append("AT RISK FOR HEART DISEASE AND KIDNEY FAILURE")
        elif patient_age > 55 and "migraines" in active_condition:
            lst.append("AT RISK FOR SEROTONIN SYNDROME")
        elif patient_age > 50 and "depression" in active_condition:
            lst.append("AT RISK FOR DEPRESSION")
        elif patient_age > 40 and "osteoporosis" in active_condition:
            lst.append("AT RISK FOR WEAK BONE DENSITY")

        if patient_age > 40 and self.sex[0]=="M":
            lst.append("AT RISK FOR TESTICULAR CANCER")
        elif patient_age > 40 and self.sex[0] == "F":
            lst.append("AT RISK FOR BREAST CANCER")
            
         else:
            pass

        return lst
        
    class Meta:
        verbose_name_plural = "Patients"


class HealthcareProviders(models.Model):
    employee_number = models.IntegerField(unique=True)
    name_title      = models.CharField(max_length=5, default="Dr.")
    first_name      = models.CharField(max_length=30, blank=True, null=True)
    last_name       = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return str(self.employee_number) + " -- " + self.first_name + " " + self.last_name

    def display(self):
        return str(self)
    class Meta:
        verbose_name_plural = "Healthcare Providers"


class Appointments(models.Model):
    healthcare_provider = models.ForeignKey(HealthcareProviders, on_delete = models.CASCADE, blank=True, null=True)
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    date = models.DateField(blank = True, null=True)
    time = models.TimeField(blank = True, null=True)

    def __str__(self):
        return str(self.date) + " " + str(self.patient)

    class Meta:
        verbose_name_plural = "Appointments"
