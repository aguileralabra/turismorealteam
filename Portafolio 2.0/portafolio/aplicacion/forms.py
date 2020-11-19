from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth import authenticate

class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Contraseña'
            }
        )
    )

    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Repetir Contraseña'
            }
        )
    )
    class Meta:
        model = User
        fields = (

            'cli_Rut',
            'cli_Nombre',
            'cli_Apellidos',
            'cli_Edad',
            'cli_Nacionalidad',
            'email',
            'cli_Telefono',
            'username'
        )
    
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseña no coinciden')

class LoginForm(forms.Form):

    username = forms.CharField(
        label='username',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder' : 'username'
            }
        )
    )

    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Contraseña'
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username= self.cleaned_data['username']
        password= self.cleaned_data['password']

        if not authenticate(username=username, password=password):
           raise forms.ValidationError('Los datos de usuario no son correcto')

        return self.cleaned_data

class UpdatePasswordForm(forms.Form):

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Contraseña Actual'
            }
        )
    )

    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Contraseña Nueva'
            }
        )
    )

class AcompañanteForm(ModelForm):
    class Meta:
        model = Acompañante
        fields = ['acom_rut','acom_nombre','acom_apellidos', 'acom_edad','acom_nacionalidad', 'acom_email', 'acom_telefono']

    def clean_acomedad(self):
        acomedad = self.cleaned_data['acom_edad']
        if acomedad < 0:
            raise forms.ValidationError('ingrese un numero mayor a 0')
        return acomedad
        
class ReservaForm(ModelForm):
    class Meta:
        model = Reserva
        fields = ['Fecha_Reserva_Inicio','Fecha_Reserva_Termino','Estado_Reserva','departamento','servicioextra']

class ReservaAdminForm(ModelForm):
    class Meta:
        model = Reserva
        fields = ['Fecha_Reserva_Inicio','Fecha_Reserva_Termino','Estado_Reserva','departamento','servicioextra','user']

class VerificationForm(forms.Form):
    codregistro = forms.CharField(required=True)

    def __init__(self, pk, *args, **kwargs):
        self.id_user = pk
        super(VerificationForm, self).__init__(*args, **kwargs)

    def clean_codregistro(self):
        codigo = self.cleaned_data['codregistro']

        if len(codigo) == 6:
            #verificamos si el codigo y el id de usuario son valido
            activo = User.objects.cod_validation(
                self.id_user,
                codigo
            )
            if not activo:
                raise form.ValidationError('el codigo es incorrecto')
        else:
            raise form.ValidationError('el codigo es incorrecto')

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('__all__')

class DepartamentoForms(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = [
            'Nombre_Departamento',
            'Numero_propiedad',
            'Descripcion_departamento', 
            'Direccion_departamento',
            'habitaciones', 
            'Baños',
            'Calefaccion',
            'Internet',
            'Amoblado',
            'Televicion', 
            'Imagen_Recinto',
            'Imagen_Entorno', 
            'Valor_Diario',
            'Disponible',
            'comuna',
            'inventario',
            'gasto']

class AdminUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['cli_Rut','cli_Nombre','cli_Apellidos', 'cli_Edad','cli_Nacionalidad', 'email','cli_Telefono','username','funcionario','is_active']

class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ['descripcion_tour','categoria','comestible', 'valor_tour','imagen_tour']

class ConductorForm(forms.ModelForm):
    class Meta:
        model = Conductor
        fields = ['cond_rut','cond_nombre','cond_apellidos', 'cond_edad','cond_nacionalidad','cond_email','cond_telefono','vehiculo']

class ServicioExtraForm(forms.ModelForm):
    class Meta:
        model = ServicioExtra
        fields = ['descrip_servicio','direccion_reunion','direccion_destino', 'fecha_encuentro','fecha_termino_servicio','valor_servicio','conductor','tour']

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['patente','color_vehiculo','cant_puerta', 'aire_acondicionado','cant_asiento','disponibilidad_vehi','imagen_vehiculo','modelo','marca']