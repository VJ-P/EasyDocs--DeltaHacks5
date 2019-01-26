from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.HCP)
admin.site.register(models.Medication)
admin.site.register(models.Side_Effects)
admin.site.register(models.Incompatible)
admin.site.register(models.Condition)
admin.site.register(models.System_Affected)
admin.site.register(models.Patient)
admin.site.register(models.Appointment)