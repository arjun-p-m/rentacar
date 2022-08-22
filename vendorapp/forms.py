from django import forms
from adminapp.models import Car, Offer

class CarForm(forms.ModelForm):
    """Form definition for Car."""

    class Meta:
        """Meta definition for Carform."""

        model = Car
        exclude = ['vendor','status','kilometer','mode']

class OfferForm(forms.ModelForm):
    """Form definition for Offer."""

    class Meta:
        """Meta definition for Offerform."""

        model = Offer
        exclude = ['status']
