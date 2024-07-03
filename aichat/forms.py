from .models import DatosUsuarios
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class DatosUserCreacionForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = DatosUsuarios
        fields = ('username', 'email')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if DatosUsuarios.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo ya esta en uso")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if DatosUsuarios.objects.filter(username=username).exists():
            raise forms.ValidationError("Este usuario ya esta en uso")
        return username