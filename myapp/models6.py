from django.db import models
from.models import Hospitals
from.models import Users,Station1

 
class Public_Enquiry(models.Model):
    enquiry_id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=100)
    Phone=models.IntegerField(null=True)
    Enquiry=models.CharField(max_length=100)
    hospital=models.ForeignKey(Hospitals,on_delete=models.CASCADE,null=True,blank=True)
    Reply=models.CharField(max_length=100)
    
