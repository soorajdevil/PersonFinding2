from django import forms
from .models import Login

class loginform(forms.ModelForm):
    class Meta:
        model=Login
        fields=['email','password']
        Widgets={
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),

        }
