from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               min_length=8,
                               max_length=32)


class RegisterForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               min_length=8,
                               max_length=32)


class RecoveryForm(forms.Form):
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))