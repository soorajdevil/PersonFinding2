from django import forms
from .models6 import Public_Enquiry

class Public_Enquiryform(forms.ModelForm):

    class Meta:
        model = Public_Enquiry
        fields = ['Name','Phone','Enquiry']
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'Enquiry': forms.Textarea(attrs={'class': 'form-control'}),
            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Name'].widget.attrs.update({'class': 'form-control-sm'}) 
        self.fields['Phone'].widget.attrs.update({'class': 'form-control-sm'}) 
        self.fields['Enquiry'].widget.attrs.update({'class': 'form-control-sm'}) 

class Public_Replyform(forms.ModelForm):

    class Meta:
        model = Public_Enquiry
        fields = ['Reply']
        widgets = {
            'Reply': forms.TextInput(attrs={'class': 'form-control'}),
            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Reply'].widget.attrs.update({'class': 'form-control-sm'})    