from django import forms

from user_profile.models import ProfilePic


class ChangeProfilePic(forms.ModelForm):
    class Meta:
        model = ProfilePic
        fields = ['profile_picture']
