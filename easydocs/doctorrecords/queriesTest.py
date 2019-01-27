from . import models

# Create your views here.
def homepage(request):
    hcpList = models.HCP.objects.all()

    print(Entry.objects.get(first_name = "Bob")
