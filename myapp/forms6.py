from django import forms
from .models3 import Casesheet
from django.core.exceptions import ValidationError

class Casesheet1(forms.ModelForm):

    GENDER_CHOICES = (
        ('M', 'Male'), ('F', 'Female'), ('O', 'Other'),
    )
    Gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    
    BLOOD_GROUP_CHOICES = (
        ('', 'Select Blood group'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )
    Blood_Group = forms.ChoiceField(choices=BLOOD_GROUP_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    
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
        model = Casesheet
        fields = ['Patient_Name', 'Blood_Group', 'Address', 'District', 'City', 'Contact_Number', 'Age', 'Gender',
                  'Description', 'Date', 'Photo', 'Patient_id']
        widgets = {
            'Patient_Name': forms.TextInput(attrs={'class': 'form-control'}),
            # 'Blood_Group': forms.TextInput(attrs={'class': 'form-control'}),
            'Address': forms.Textarea(attrs={'class': 'form-control'}),
            # 'District': forms.TextInput(attrs={'class': 'form-control'}),
            'City': forms.TextInput(attrs={'class': 'form-control'}),
            'Contact_Number': forms.NumberInput(attrs={'class': 'form-control'}),
            'Age': forms.NumberInput(attrs={'class': 'form-control'}),
            # 'Gender': forms.TextInput(attrs={'class': 'form-control'}),
            'Description': forms.TextInput(attrs={'class': 'form-control'}),
            'Date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Photo': forms.FileInput(attrs={'class': 'form-control'}),
            'Patient_id': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(Casesheet1, self).__init__(*args, **kwargs)
        self.fields['Photo'].required = False  # Set Photo field as not required
    
    def clean_Phone(self):
        phone = self.cleaned_data.get('Contact_Number')
        if len(phone) != 10:
            raise ValidationError("Phone number must be 10 characters long")
        return phone