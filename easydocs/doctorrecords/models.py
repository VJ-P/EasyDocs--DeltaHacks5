from django.db import models

# Create your models here.
class HCP(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Medication(models.Model):
    name = models.CharField(max_length=30)

class Side_Effects(models.Model):
    side_effect = models.CharField(max_length=30)
    medication = models.ForeignKey('Medication', on_delete = models.CASCADE)


class Incompatible(models.Model):
    medication_1 = models.ForeignKey('Medication', on_delete = models.CASCADE)
    medication_2 = models.ForeignKey('Medication', on_delete = models.CASCADE)

class Condition(models.Model):
    name = models.CharField(max_length=30)
    medication = models.ForeignKey('Medication', on_delete = models.CASCADE)
    prompt = models.ForeignKey('Prompt', on_delete = models.CASCADE)

class System_Affected(models.Model):
    system = models.CharField(max_length=30)
    condition = models.ForeignKey('Condition', on_delete = models.CASCADE)
    prompt = models.ForeignKey('Prompt', on_delete = models.CASCADE)

class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    condition = models.ForeignKey( 'Condition', on_delete = models.CASCADE)

class Prompt(models.Model):
    message = models.TextField()
