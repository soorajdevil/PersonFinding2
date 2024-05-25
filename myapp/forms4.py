from django import forms
from .models1 import Usermissingadds

class UserMissingform(forms.ModelForm):
    GENDER_CHOICES = (
        ('M', 'Male'), ('F', 'Female'), ('O', 'Other'),
    )

    Gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    
    # Use DateInput widget for Missing_date
    Missing_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
    )

    # Allow input for height in centimeters or inches
    Height = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    # Allow input for weight in kilograms
    Weight = forms.DecimalField(max_digits=5, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Usermissingadds
        fields = ['Name', 'Age', 'Height', 'Weight', 'Missing_date', 'Missing_place', 'Other_details', 'Gender', 'Photo']
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Age': forms.NumberInput(attrs={'class': 'form-control'}),
            'Height': forms.NumberInput(attrs={'class': 'form-control'}),
            'Weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'Missing_date': forms.NumberInput(attrs={'class': 'form-control'}),
            'Missing_place': forms.TextInput(attrs={'class': 'form-control'}),
            'Other_details': forms.TextInput(attrs={'class': 'form-control'}),
            'Photo': forms.FileInput(attrs={'class': 'form-control'}),
            'Gender': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Name'].widget.attrs.update({'class': 'form-control-sm'})
        self.fields['Age'].widget.attrs.update({'class': 'form-control-sm'})
        self.fields['Missing_date'].widget.attrs.update({'class': 'form-control-sm'})
        self.fields['Missing_place'].widget.attrs.update({'class': 'form-control-sm'})
        self.fields['Other_details'].widget.attrs.update({'class': 'form-control-sm'})
