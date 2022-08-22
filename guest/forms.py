from django import forms
from adminapp.models import User

class UserForm(forms.ModelForm):
    """Form definition for User."""

    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = ('first_name','last_name','email','phone','address','username','password',)
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'last_name': forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'email': forms.EmailInput(
                attrs={'class':'form-control'}
            ),
            'phone': forms.NumberInput(
                attrs={'class':'form-control','value':''}
            ),
            'address': forms.Textarea(
                attrs={'class':'form-control'}
            ),
            'username': forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'password': forms.PasswordInput(
                attrs={'class':'form-control'}
            ),
        }
        help_texts = {'username':None}

class VendorForm(forms.ModelForm):
    """Form definition for User."""

    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = ('first_name','last_name','email','phone','address','company_name','username','password',)
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'last_name': forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'email': forms.EmailInput(
                attrs={'class':'form-control'}
            ),
            'phone': forms.NumberInput(
                attrs={'class':'form-control','value':''}
            ),
            'address': forms.Textarea(
                attrs={'class':'form-control'}
            ),
            'company_name': forms.TextInput(
                attrs={'class':'form-control','value':'nn'}
            ),
            'username': forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'password': forms.PasswordInput(
                attrs={'class':'form-control'}
            ),
        }
        help_texts = {'username':None}


