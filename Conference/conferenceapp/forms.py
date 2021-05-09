from django import forms
from conferenceapp.models import Registrationform 


class RegistrationForm(forms.ModelForm):
    name                 = forms.CharField(widget=forms.TextInput(attrs={ "type":"text", "class":"form-control", "placeholder":"Your Name", "id":"fname", "name":"name"  }))
    email                = forms.CharField(widget=forms.TextInput(attrs={"type":"email", "class":"form-control",  "placeholder":"Email", "id":"lname","name":"email"  }))
    district             = forms.CharField(widget=forms.TextInput(attrs={ "type":"text", "class":"form-control",  "placeholder":"District", "id":"email", "name":"name" }))
    profession          = forms.CharField(widget=forms.TextInput(attrs={  "type":"text", "class":"form-control",  "placeholder": "Phone", "id":"cell", "name":"name"}))
   
    class Meta:
        model = Registrationform
        fields ='__all__'

 