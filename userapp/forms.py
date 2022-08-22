from django import forms
from django.db.models import fields
from django.forms.widgets import Textarea
from adminapp.models import User, Order, UserComplaints, BookTaxi

class ProfileForm(forms.ModelForm):
    """Form definition for User."""

    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = ('email','phone','address','username',)
        widgets = {
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
        }
        help_texts = {'username':None}

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class DateTime(forms.DateTimeInput):
    input_type = 'datetime-local'

class OrderForm(forms.ModelForm):
    """Form definition for Order."""

    class Meta:
        """Meta definition for Orderform."""

        model = Order
        fields = ['pick_up_location','pick_date','pick_time','return_date','return_time']
        widgets = {
            'pick_up_location': forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'pick_date': DateInput(
                attrs={'class':'form-control'}
            ),
            'pick_time': TimeInput(
                attrs={'class':'form-control'}
            ),
            'return_date': DateInput(
                attrs={'class':'form-control'}
            ),
            'return_time': TimeInput(
                attrs={'class':'form-control'}
            ),
        }

class ComplaintsForm(forms.ModelForm):
    """Form definition for Complaints."""

    class Meta:
        """Meta definition for Complaintsform."""

        model = UserComplaints
        exclude = ('status','user',)
        widgets = {
            'c_type': forms.Select(
                attrs={'class':'form-control'}
            ),
            'description': Textarea(
                attrs={'class':'form-control','rows':3}
            ),
        }

class TaxiBookForm(forms.ModelForm):
    """Form definition for Order."""

    class Meta:
        """Meta definition for Orderform."""

        model = BookTaxi
        fields = ['start_from','to_location','date']
        widgets = {
            'start_from': forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'to_location': forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'date': DateTime(
                attrs={'class':'form-control'}
            ),
        }

