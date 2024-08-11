from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class ProfileForm( forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image', 'name', 'description', 'website']

    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=False)

    class Meta:
        model = UserProfile
        fields= ['image', 'name', 'description', 'website']

    def save(self, commit=True):
        user_profile = super(ProfileForm, self).save(commit=False)
        user = user_profile.user
        user.email = self.cleaned_data['email']

        if self.cleaned_data['password']:
            user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()
            user_profile.save()
        return user_profile