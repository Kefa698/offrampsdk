from django.db import models

# Create your models here.
class mobile(models.Model):
    amount = models.DecimalField(decimal_places=2,max_digits=11,default=1)
    mobile_number = models.CharField(max_length=12)