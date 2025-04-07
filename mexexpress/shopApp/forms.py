from django import forms
from django.core import validators


def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError('no empieza con z')
class FormComment(forms.Form):
    full_name = forms.CharField(label='Nombre',validators=[validators.MaxLengthValidator(20),check_for_z])
    email = forms.EmailField(label='Email')
    comment = forms.CharField(label='Comentario',widget=forms.Textarea,validators=[validators.MaxLengthValidator(150)])

class FormContact(forms.Form):
    full_name = forms.CharField(label="Nombre ",max_length=255,required=True)
    address = forms.CharField(label="direccion ",max_length=255,required=True)
    phone = forms.CharField(label="Telefono ",max_length=15,required=True)
    email = forms.EmailField(label="Email ",max_length=155,required=True)
    activate = forms.BooleanField(required=True)



