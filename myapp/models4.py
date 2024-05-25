from django.db import models
from.models import Hospitals
from.models import Users,Station1

 
class Enquiry(models.Model):
    Enquiry_detail=models.CharField(max_length=100)
    user_id=models.ForeignKey(Users,on_delete=models.CASCADE,null=True,blank=True)
    Current_Date =models.DateField()
    hospital=models.ForeignKey(Hospitals,on_delete=models.CASCADE,null=True,blank=True)
    station_id=models.ForeignKey(Station1,on_delete=models.CASCADE,null=True,blank=True)
    Reply=models.CharField(max_length=100)
    enquiry_id=models.IntegerField(primary_key=True)


