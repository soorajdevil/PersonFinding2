from django import forms
from .models import Station1
from django.core.exceptions import ValidationError
import re

class Policeform(forms.ModelForm):
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
        model = Station1
        fields = ['Station_id', 'Address_line1', 'Address_line2', 'District', 'City', 'Pin', 'Contact_number', 'Email', 'Password']
        widgets = {
            'Station_id': forms.TextInput(attrs={'class': 'form-control'}),
            'Address_line1': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'cols': 40}),  # Adjust rows and cols as needed
            'Address_line2': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'cols': 40}),  # Adjust rows and cols as needed
            'District': forms.TextInput(attrs={'class': 'form-control'}),
            'City': forms.TextInput(attrs={'class': 'form-control'}),
            'Pin': forms.NumberInput(attrs={'class': 'form-control'}),
            'Contact_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'Email': forms.TextInput(attrs={'class': 'form-control'}),
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
        phone = self.cleaned_data.get('Contact_number')
        if len(phone) != 10:
            raise ValidationError("Phone number must be 10 characters long")
        return phone
