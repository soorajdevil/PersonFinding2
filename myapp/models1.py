from django.db import models
 
class Usermissingadds(models.Model):
    Name=models.CharField(max_length=100)
    Gender=models.CharField(max_length=100)
    Age=models.IntegerField(null=True)
    Height=models.CharField(max_length=100)
    Weight=models.CharField(max_length=100)
    Missing_date=models.DateField(max_length=100)
    Missing_place=models.CharField(max_length=100)
    Other_details=models.CharField(max_length=100)
    Pass_to_public=models.IntegerField(null=True)
    Photo=models.ImageField(upload_to='uploads/')