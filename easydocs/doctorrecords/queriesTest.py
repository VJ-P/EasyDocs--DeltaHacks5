from . import models

# Create your views here.

hcpList = models.HCP.objects.all()

print(models.HCP.objects.get(first_name="Bob"))
