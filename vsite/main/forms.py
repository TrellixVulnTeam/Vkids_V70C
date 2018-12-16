from django import forms

from django.db import transaction

from .models import Location,Bus,School 

class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ('bus_number',)
    
    @staticmethod
    def addBusForm(request, admin):
        bus_form = BusForm(request.POST)
        if bus_form.is_valid():
            bus_form = bus_form.save(False)
            bus_form.school = admin.school
            print(bus_form.school)
            bus_form.save()

            return request

class LocationForm(forms.ModelForm ):
    class Meta:
        model = Location
        exclude = ('location_id',)
    
