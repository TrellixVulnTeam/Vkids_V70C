from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from user.models import User
from person.models import Parent, Admin


class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        exclude = ('user',)

class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        exclude = ('user',)

class RegistrationForm(UserCreationForm):

    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = (  
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2'
        )

    @transaction.atomic
    def save(self, is_boss, is_parent, commit = True):
        user = super(RegistrationForm,self).save(commit=False)
        user.is_boss = is_boss
        user.is_parent = is_parent
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

