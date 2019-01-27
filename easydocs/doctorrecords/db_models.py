from django.db import models

class SideEffects(models.Model):
    effect = models.CharField(max_length = 100, blank=True, null=True)

    def __str__(self):
        return self.effect

class Treatments(models.Model):
    name                    = models.CharField(max_length=30, blank=True, null=True)
    new                     = models.BooleanField(default=False)
    side_effects            = models.ManyToManyField(SideEffects, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Treatments"


class Conditions(models.Model):
    name                    = models.CharField(max_length=30, blank=True, null=True)
    treatments              = models.ManyToManyField(Treatments)
    side_effects            = models.ManyToManyField(SideEffects, blank=True, null=True)

    def __str__(self):
        return self.name

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

    class Meta:
        verbose_name_plural = "Active Conditions"



class Incompatibilities(models.Model):
    treatment             = models.ForeignKey(Treatments, on_delete=models.CASCADE, related_name="treatment_queried")
    incompat_treatments   = models.ForeignKey(Treatments, on_delete=models.CASCADE, related_name="treatment_compared_to")
    incompat_conditions   = models.ForeignKey(Conditions, on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural = "Incompatabilities"

    def __str__(self):
        return self.treatment

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
        return str(self.addr_line_1) + ", " + str(self.addr_line_2) + ", " + str(self.city) + ", " + str(self.province) + ", " + str(self.country) + ", " + str(self.postal_code)

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
        return str(self.healthcare_provider) + " - " + str(self.patient) + ": " + str(self.date) + " - " + str(self.time)

    class Meta:
        verbose_name_plural = "Appointments"
