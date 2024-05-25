from django.db import models
from.models1 import Usermissingadds
from.models import Station1
 
class Missing_found(models.Model):
    missing_id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=100)
    Phone=models.IntegerField(null=True)
    District=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    Street=models.CharField(max_length=100)
    Other_details=models.CharField(max_length=100)
    Found_date=models.DateField()
    found_Usermissing=models.ForeignKey(Usermissingadds,on_delete=models.CASCADE,null=True,blank=True)
    Photo=models.ImageField(upload_to='uploads/') 
    pass_to_police=models.ForeignKey(Station1,on_delete=models.CASCADE,null=True,blank=True)