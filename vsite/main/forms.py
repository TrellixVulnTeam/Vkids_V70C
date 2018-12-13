from django import forms

from django.db import transaction

from .models import Location 

class LocationForm(forms.ModelForm ):
    class Meta:
        model = Location
        exclude = ('location_id',)
    
