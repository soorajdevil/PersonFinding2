from django import forms
from .models4 import Enquiry

class Enquiryform(forms.ModelForm):

    class Meta:
        model = Enquiry
        fields = ['Enquiry_detail']
        widgets = {
            'Enquiry_detail': forms.TextInput(attrs={'class': 'form-control'}),
            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Enquiry_detail'].widget.attrs.update({'class': 'form-control-sm'})    

class Replyform(forms.ModelForm):

    class Meta:
        model = Enquiry
        fields = ['Reply']
        widgets = {
            'Reply': forms.TextInput(attrs={'class': 'form-control'}),
            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Reply'].widget.attrs.update({'class': 'form-control-sm'})    