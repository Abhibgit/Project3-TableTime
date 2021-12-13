from django.forms import ModelForm
from .models import Profile, User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class ProfileForm(UserCreationForm):
    first_name = forms.CharField(max_length = 100)
    last_name = forms.CharField(max_length = 100)
    email = forms.EmailField(max_length=100)
    phone = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ("username","first_name", "last_name", "email", "phone", "address")

    def save(self, commit=True):
        user = super(ProfileForm, self).save(commit=False)
        print(user)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            profile = Profile(phone = self.cleaned_data["phone"], address = self.cleaned_data["address"], user = user)
            profile.save()
        return user
