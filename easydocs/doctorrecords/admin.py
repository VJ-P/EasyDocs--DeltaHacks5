from django.contrib import admin
from . import db_models
# Register your models here.


admin.site.register(db_models.HealthcareProviders)
admin.site.register(db_models.Patient)
admin.site.register(db_models.Appointments)
admin.site.register(db_models.FamilyHistory)


admin.site.register(db_models.Treatments)
admin.site.register(db_models.ActiveConditions)
admin.site.register(db_models.Conditions)
admin.site.register(db_models.Incompatibilities)
admin.site.register(db_models.SideEffects)
