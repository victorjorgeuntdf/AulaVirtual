from django import forms
from django.core.exceptions import ValidationError

class AltaAlumnoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True,widget=forms.TextInput(attrs={'class': 'campo_azul'}))
    apellido = forms.CharField(label="Apellido", required=True)
    dni = forms.IntegerField(label="DNI", required=True)
    email = forms.EmailField(label="email", required=True)
    direccion = forms.CharField(label="Dirección", required=True)

    CHOISES = (('Option 1', 'Option 1'), ('Option 2', 'Option 2'))
    fields = forms.ChoiceField(choices=CHOISES)

    def clean_nombre(self):
        if not self.cleaned_data["nombre"].isalpha():
            raise ValidationError("El Nombre solo puede estar compuesto por letras")
        """ 
        puedo transformar al texto en mayuculas
        self.cleaned_data["nombre"] = self.cleaned_data["nombre"].upper() """
        return self.cleaned_data["nombre"]
    
    def clean_apellido(self):
        if not self.cleaned_data["apellido"].isalpha():
            raise ValidationError("El Apellido solo puede estar compuesto por letras")
        return self.cleaned_data["apellido"]
    
    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get("nombre")
        apellido = cleaned_data.get("apellido")
        if  nombre == "Carlos" and apellido == "Lopez":
            raise ValidationError("El usuario Carlos Lopez ya esta registrado")
        if self.cleaned_data["dni"] < 1000000:
                raise ValidationError("El DNI debe tener 8 digitos")
        return self.cleaned_data
    