from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class newForm(UserCreationForm):
    email=forms.EmailField(required=True)

    class Meta():
        model=User
        fields=("username", "email", "password1","password2")

        def save(self, commit=True):
            user=super(newForm, self).save(commit=False)
            user.email=self.cleaned_data['email']
            if commit:
                user.save()
            return user

class contact_form(forms.Form):
    Name=forms.CharField(required=True)
    Email=forms.CharField(required=True)
    Message=forms.CharField(required=True, widget=forms.Textarea, max_length=1000)