from pyexpat import model
from attr import fields
from django.contrib.auth.models import User
from django import forms
from . models import Work

class SignUpform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password']

class Update_form(forms.ModelForm):
    class Meta:
        model = Work
        fields = ['place','Name','about_work','amount']        

