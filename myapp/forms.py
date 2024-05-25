from django import forms
import re
from .models import Users
from django.core.exceptions import ValidationError

class Userform(forms.ModelForm):
    DISTRICT_CHOICES = (
        ('', 'Select District'),
        ('Thiruvananthapuram', 'Thiruvananthapuram'),
        ('Kollam', 'Kollam'),
        ('Pathanamthitta', 'Pathanamthitta'),
        ('Alappuzha', 'Alappuzha'),
        ('Kottayam', 'Kottayam'),
        ('Idukki', 'Idukki'),
        ('Ernakulam', 'Ernakulam'),
        ('Thrissur', 'Thrissur'),
        ('Palakkad', 'Palakkad'),
        ('Malappuram', 'Malappuram'),
        ('Kozhikode', 'Kozhikode'),
        ('Wayanad', 'Wayanad'),
        ('Kannur', 'Kannur'),
        ('Kasaragod', 'Kasaragod'),
    )

    District = forms.ChoiceField(choices=DISTRICT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model=Users
        fields = ['Name', 'Phone', 'Email', 'District', 'Pin', 'Password']
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control'}),
            # 'District': forms.TextInput(attrs={'class': 'form-control'}),
            'Pin': forms.NumberInput(attrs={'class': 'form-control'}),
            'Password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def clean_Password(self):
        password = self.cleaned_data.get('Password')
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long")
        if not any(char.isdigit() for char in password):
             raise ValidationError("Password must contain at least one digit.")
        return password
    
    def clean_Phone(self):
        phone = self.cleaned_data.get('Phone')
        if len(phone) != 10:
            raise ValidationError("Phone number must be 10 characters long")
        return phone
