from django.db import models
import datetime

# Create your models here.
class HCP(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name_plural = "HCP"

class Medication(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Medication"

class Date(models.Model):
    start_date = models.DateField()
    end_date= models.DateField()

class Side_Effects(models.Model):
    side_effect = models.CharField(max_length=30)
    medication = models.ForeignKey('Medication', on_delete = models.CASCADE)
    
    def __str__(self):
        return self.side_effect

    class Meta:
        verbose_name_plural = "Side_Effects"

class Incompatible(models.Model):
    medication = models.TextField(max_length = 1024*2)
    #medication_2 = models.ForeignKey('Medication', on_delete = models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Incompatible"
    
    def __str__(self):
        return self.medication_1
    
class Condition(models.Model):
    name = models.CharField(max_length=30)
    medication = models.ForeignKey('Medication', on_delete = models.CASCADE)
    #prompt = models.ForeignKey('Prompt', on_delete = models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Condition"

class System_Affected(models.Model):
    system = models.CharField(max_length=30)
    condition = models.ForeignKey('Condition', on_delete = models.CASCADE)
    #prompt = models.ForeignKey('Prompt', on_delete = models.CASCADE)
    
    def __str__(self):
        return self.system
    
    class Meta:
        verbose_name_plural = "System Affected"
    
class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    condition = models.ForeignKey( 'Condition', on_delete = models.CASCADE)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
    class Meta:
        verbose_name_plural = "Patient"

class Appointment(models.Model):
    doctor = models.ForeignKey(HCP, on_delete = models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    date = models.DateField(blank = True, null = True)
    time = models.TimeField(blank = True, null = True)
    
    def __str__(self):
        return self.doctor + " - " + self.patient + ": " + self.date + " - " + self.time
    
    class Meta:
        verbose_name_plural = "Appointment"