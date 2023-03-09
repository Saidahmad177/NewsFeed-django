from django import forms
from django.contrib.auth.models import User
from users.models import Profile


class SignUp(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', ]

    def clean_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.data.get('password2')
        if password != confirm_password:
            print('nooonononsodfnasodfaskdfasdfj;laskdjf;asldjkf;asldkjfas')

        return self.cleaned_data.get('password')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('sdfsdfsdfsdf')
        return username


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user_image']


class UpdateProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email']

