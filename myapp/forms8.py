from django import forms
from .models5 import Complaint

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['Name', 'Complaint']
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Complaint': forms.TextInput(attrs={'class': 'form-control'}),
            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Complaint'].widget.attrs.update({'class': 'form-control-sm'})    