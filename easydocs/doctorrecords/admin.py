from django.contrib import admin
from . import db_models
# Register your models here.
admin.site.register(db_models.HCP)
admin.site.register(db_models.Medication)
admin.site.register(db_models.Side_Effects)
admin.site.register(db_models.Incompatible)
admin.site.register(db_models.Condition)
admin.site.register(db_models.System_Affected)
admin.site.register(db_models.Patient)
admin.site.register(db_models.Appointment)