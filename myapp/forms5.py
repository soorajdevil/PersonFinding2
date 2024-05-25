from django import forms
from .models2 import Accidents
from django.core.exceptions import ValidationError

class Accidentform(forms.ModelForm):

    class Meta:
        model = Accidents
        fields = ['Name', 'Contact_Number', 'Accident_Details', 'Location','Image','Video']
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Contact_Number': forms.TextInput(attrs={'class': 'form-control'}),
            'Accident_Details': forms.TextInput(attrs={'class': 'form-control'}),
            'Location': forms.TextInput(attrs={'class': 'form-control'}),
            'Image': forms.FileInput(attrs={'class': 'form-control'}),
            'Video': forms.FileInput(attrs={'class': 'form-control'}),
            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Name'].widget.attrs.update({'class': 'form-control-sm'})
        self.fields['Contact_Number'].widget.attrs.update({'class': 'form-control-sm'})
        self.fields['Accident_Details'].widget.attrs.update({'class': 'form-control-sm'})
        self.fields['Location'].widget.attrs.update({'class': 'form-control-sm'})
        self.fields['Image'].required = False  # Set Photo field as not required
        self.fields['Video'].required = False  # Set Photo field as not required

    def clean_Phone(self):
        phone = self.cleaned_data.get('Contact_Number')
        if len(phone) != 10:
            raise ValidationError("Phone number must be 10 characters long")
        return phone