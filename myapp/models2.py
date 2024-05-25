from django.db import models
 
class Accidents(models.Model):
    Name=models.CharField(max_length=100)
    Contact_Number=models.CharField(max_length=100)
    Accident_Details =models.CharField(max_length=100)
    Location=models.CharField(max_length=100)
    Image=models.FileField(upload_to='uploads/')
    Video=models.FileField(upload_to='uploads/')
   