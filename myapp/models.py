from django.db import models
 
class Users(models.Model):
    Name=models.CharField(max_length=100)
    Phone=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    District=models.CharField(max_length=100)
    Pin=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    user_id=models.IntegerField(primary_key=True)
    usertype=models.CharField(max_length=100,default='User')


 
class Station1(models.Model):
    Station_id=models.IntegerField(null=True)
    Address_line1=models.CharField(max_length=100)
    Address_line2=models.CharField(max_length=100)
    District=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    Pin=models.IntegerField(null=True)
    Contact_number=models.IntegerField(null=True)
    Email=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    usertype=models.CharField(max_length=100,default='Police')




class Hospitals(models.Model):
    Hospital_Name=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    District=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    Contact_number=models.IntegerField(null=True)
    Email=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    hospital_id=models.IntegerField(primary_key=True)
    usertype=models.CharField(max_length=100,default='Hospitals')
    proof=models.ImageField(upload_to='uploads/')



class Login(models.Model):
     email=models.CharField(max_length=100)
     password=models.CharField(max_length=100)


 
