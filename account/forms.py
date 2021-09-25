from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation


###########  دیگه استفاده نمیشه #################
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your username or email', 'autocomplete': 'off'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
                                                            'autocomplete': 'off',
                                                        }))
#############################################



class UserRegistrationForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
    }
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder':'Enter your pass',
        'autocomplete': 'new-password'}),
        validators=[password_validation.validate_password])
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email','first_name')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder':'Enter your username or email', 'autocomplete': 'new-username'}),
            'email': forms.EmailInput(attrs={'required': True, 'placeholder':'Enter your email'}),
            # or 'password': forms.PasswordInput(attrs={'placeholder':'Enter your pass', 'autocomplete': 'new-password'}),
        }
        labels = {
            'email': _('Your Email'),
        }
        error_messages = {
            'username': {
                'max_length': _("This username is too for Bookmarks."),
            },
        }
        help_texts = {
            'email': _('your email can help you.'),
        }
        field_classes={

        }


    def clean_password2(self):
        # همیشه از متد get استفاده کنید
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise forms.ValidationError(self.error_messages['password_mismatch'],
                code='password_mismatch',)
        return password2


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')
