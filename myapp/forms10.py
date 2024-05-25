from django import forms
from .models7 import Missing_found
from django.core.exceptions import ValidationError
import re

class Found(forms.ModelForm):
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
        model = Missing_found
        fields = ['Name', 'Phone', 'District', 'City', 'Street', 'Other_details', 'Found_date', 'Photo']
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Phone': forms.TextInput(attrs={'class': 'form-control'}),
            'District': forms.TextInput(attrs={'class': 'form-control'}),
            'City': forms.TextInput(attrs={'class': 'form-control'}),
            'Street': forms.TextInput(attrs={'class': 'form-control'}),
            'Other_details': forms.TextInput(attrs={'class': 'form-control'}),
            'Found_date': forms.TextInput(attrs={'class': 'form-control'}),
            'Photo': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def clean_Phone(self):
        phone = self.cleaned_data.get('Phone')
        if len(phone) != 10:
            raise ValidationError("Phone number must be 10 characters long")
        return phone
