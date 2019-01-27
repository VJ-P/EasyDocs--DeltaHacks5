from django.db import models
import datetime


class HCP(models.Model):
    employee_number = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
    def __str__(self):
        return str(self.employee_number) + " -- " + self.first_name + " " + self.last_name

    class Meta:
        verbose_name_plural = "Healthcare Providers"

class Medication(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Medications"

class Side_Effects(models.Model):
    side_effect = models.CharField(max_length=30)
    medication = models.ForeignKey('Medication', on_delete = models.CASCADE)
    
    def __str__(self):
        return self.side_effect

    class Meta:
        verbose_name_plural = "Side Effects"

class Incompatible(models.Model):
    medication = models.TextField(max_length = 1024*2)
    
    class Meta:
        verbose_name_plural = "Incompatabilities"
    
    def __str__(self):
        return self.medication
    
class Condition(models.Model):
    name = models.CharField(max_length=30)
    medication = models.ForeignKey('Medication', on_delete = models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Health Conditions"

class System_Affected(models.Model):
    system = models.CharField(max_length=30)
    condition = models.ForeignKey('Condition', on_delete = models.CASCADE)
    
    def __str__(self):
        return self.system
    
    class Meta:
        verbose_name_plural = "Systems Affected"
    
class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    condition = models.ForeignKey( 'Condition', on_delete = models.CASCADE)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
    class Meta:
        verbose_name_plural = "Patients"

class Appointment(models.Model):
    doctor = models.ForeignKey(HCP, on_delete = models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    date = models.DateField(blank = True, null = True)
    time = models.TimeField(blank = True, null = True)
    
    def __str__(self):
        return str(self.doctor) + " - " + str(self.patient) + ": " + str(self.date) + " - " + str(self.time)
    
    class Meta:
        verbose_name_plural = "Appointments"