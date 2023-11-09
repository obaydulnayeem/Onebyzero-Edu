from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile
from study.models import University, Department

class SignupForm(UserCreationForm):   
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        
     # Customize the labels, help_text, and placeholders
    username = forms.CharField(
        label='',  # Empty label
        help_text='',  # Empty help text
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password1 = forms.CharField(
        label='',  # Empty label
        help_text='',  # Empty help text
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )
    password2 = forms.CharField(
        label='',  # Empty label
        help_text='',  # Empty help text
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})
    )


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

# class UserEditForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['user', 'user_type', 'bio', 'email']
        

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'bio', 'user_type', 'profile_image', 'email', 'university', 'department', 'year', 'semester']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =  ['bio', 'user_type', 'profile_image', 'email', 'university', 'department', 'year', 'semester']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department'].queryset = Department.objects.none()

        if 'university' in self.data:
            try:
                university_id = int(self.data.get('university'))
                self.fields['department'].queryset = Department.objects.filter(university_id=university_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance and self.instance.university: 
            self.fields['department'].queryset = self.instance.university.department_set.order_by('name')
