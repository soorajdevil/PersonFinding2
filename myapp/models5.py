from django.db import models

class Complaint(models.Model):
    Name = models.CharField(max_length=100)
    Complaint= models.TextField()
    Date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Complaint from {self.Name}"