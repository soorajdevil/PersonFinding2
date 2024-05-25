from django.db import models

class Casesheet(models.Model):
    Patient_Name=models.CharField(max_length=100)
    Blood_Group=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    District=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    Contact_Number=models.CharField(max_length=100)
    Age=models.IntegerField(null=True)
    Gender=models.CharField(max_length=100)
    Description=models.CharField(max_length=100)
    Date=models.CharField(max_length=100)
    Photo=models.ImageField(upload_to='uploads/') 
    Patient_id=models.IntegerField(primary_key=True)
   
   

   