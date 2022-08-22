from django import forms
from adminapp.models import Car

class CarForm(forms.ModelForm):
    """Form definition for Car."""

    class Meta:
        """Meta definition for Carform."""

        model = Car
        exclude = ['vendor','status','mode']