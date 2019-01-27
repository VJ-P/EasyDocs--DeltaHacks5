
# Create your views here.

models.Appointment.objects.filter(doctor__first_name="Bob").filter(date__range=["2019-01-05", "2019-01-26"])
