from django import forms

class FormComment(forms.Form):
    full_name = forms.CharField(label='Nombre')
    email = forms.EmailField(label='Email')
    comment = forms.CharField(label='Comentario',widget=forms.Textarea)

class FormContact(forms.Form):
    full_name = forms.CharField(label="Nombre ",max_length=255,required=True)
    address = forms.CharField(label="direccion ",max_length=255,required=True)
    phone = forms.CharField(label="Telefono ",max_length=15,required=True)
    email = forms.EmailField(label="Email ",max_length=155,required=True)
    activate = forms.BooleanField(required=True)



