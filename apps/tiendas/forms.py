from django import forms

from apps.tiendas.models import Tienda


class CrearTiendaForm(forms.ModelForm):


    class Meta:
        model = Tienda
        fields=(
            'nombre',
            'direccion',
            'correo',
            'telefono',
            'estatus',
        )
        widgets = {
            # 'clave': forms.HiddenInput(),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
        }

