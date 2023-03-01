from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .models import Profile
import datetime



class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta():
        model = User
        fields = ['username','email','password1','password2']
    
    def save(self,commit =True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    

class ProfileForm(UserChangeForm):
    birth_date = forms.DateField(initial=datetime.date.today)
    bio = forms.Textarea()
    password = None
    class Meta():
        model = Profile
        fields = ['birth_date','bio']
