from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from django.conf import settings
from datetime import datetime
from django.db.models.signals import post_save
import random

def random_string():
    return str(random.randint(10000, 99999))

class User(AbstractBaseUser, PermissionsMixin):
    cli_Rut=models.CharField('Rut',max_length=30, unique=True)
    cli_Nombre=models.CharField('Nombre',max_length=30, blank=True)
    cli_Apellidos=models.CharField('Apellidos',max_length=30, blank=True)
    cli_Edad= models.IntegerField('Edad', blank=True, null=True)
    cli_Nacionalidad=models.CharField('Nacionalidad',max_length=30, blank=True)
    email= models.EmailField('Correo', blank=True)
    cli_Telefono=models.CharField('Telefono',max_length=15, blank=True)
    username = models.CharField(max_length=10, unique=True)
    codregistro = models.CharField(max_length=6, blank=True, default='000000')
    funcionario = models.BooleanField(default=False)
    #
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False) 

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['cli_Rut', 'cli_Nombre','cli_Apellidos','cli_Edad','cli_Nacionalidad','email','cli_Telefono']

    objects = UserManager()

    def get_full_name (self):
        return self.cli_Nombre + ' ' + self.cli_Apellidos

class Acompañante(models.Model):
    acom_rut=models.CharField('Rut',max_length=14, unique=True)
    acom_nombre=models.CharField('Nombre',max_length=30)
    acom_apellidos=models.CharField('Apellidos',max_length=30)
    acom_edad= models.IntegerField('Edad',null=True)
    acom_nacionalidad=models.CharField('Nacionalidad',max_length=30)
    acom_email= models.EmailField('Correo', unique=True)
    acom_telefono=models.CharField('Telefono',max_length=12)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__ (self):
        return self.acom_rut

#def quitar_relacion_user_acompañante(sender, instance, **kwargs):
#    usuario = instance.id
#    acompañantes = Acompañante.objects.filter(user_id=usuario)
#    for acompañantt in acompañantes:
#        acompañantt.user_id.remove(usuario)

#post_save.connect(quitar_relacion_user_acompañante, sender = User)

class Inventario(models.Model):
    reparacion= models.CharField(max_length=100, default="")
    mejoramiento= models.CharField(max_length=100, default="")

    def __str__ (self):
        return self.reparacion

class Gasto(models.Model):
    dividendo = models.IntegerField()
    contribucion = models.IntegerField()

class Ciudad(models.Model):
    descrip_ciudad=models.CharField(max_length=100, default="")

    def __str__ (self):
        return self.descrip_ciudad

class Comuna(models.Model):
    descrip_comuna=models.CharField(max_length=100, default="")
    ciudad=models.ForeignKey(Ciudad, on_delete=models.CASCADE)

    def __str__ (self):
        return self.descrip_comuna

class Departamento(models.Model):

    CALE_CHOICES = (
        ('Si', 'Si'),
        ('No', 'No'),
    )
    INTERNET_CHOICES = (
        ('Si', 'Si'),
        ('No', 'No'),
    )
    AMOBLADO_CHOICES = (
        ('Si', 'Si'),
        ('No', 'No'),
    )
    TELEVICION_CHOICES = (
        ('Si', 'Si'),
        ('No', 'No'),
    )
    DISPONIBILIDADDEPART_CHOICES = (
        ('Si', 'Si'),
        ('No', 'No'),
    )
    Nombre_Departamento = models.CharField(max_length=30)
    Numero_propiedad = models.IntegerField(null=True)
    Descripcion_departamento= models.CharField(max_length=200, default="")
    Direccion_departamento= models.CharField(max_length=200, default="")
    habitaciones = models.IntegerField(null=True)
    Baños = models.IntegerField(null=True)    
    Calefaccion = models.CharField(max_length=2, choices=CALE_CHOICES)
    Internet = models.CharField(max_length=2, choices=INTERNET_CHOICES)
    Amoblado = models.CharField(max_length=2, choices=AMOBLADO_CHOICES)
    Televicion = models.CharField(max_length=2, choices=TELEVICION_CHOICES)
    Imagen_Recinto = models.ImageField( default="", blank=True, null=True)
    Imagen_Entorno = models.ImageField( default="", blank=True, null=True)
    Valor_Diario = models.IntegerField()
    Disponible = models.CharField(max_length=2, choices=DISPONIBILIDADDEPART_CHOICES)
    comuna=models.ForeignKey(Comuna, on_delete=models.CASCADE, default="")
    inventario = models.OneToOneField(Inventario, unique=True, on_delete=models.CASCADE, default="")
    gasto = models.OneToOneField(Gasto, unique=True, on_delete=models.CASCADE, default="")

    def __str__ (self):
        return self.Nombre_Departamento

class Vehiculo(models.Model):
    AIRE_CHOICES = (
        ('Si', 'Si'),
        ('No', 'No'),
    )
    DISPONIBILIDADVEHICULO_CHOICES = (
        ('Si', 'Si'),
        ('No', 'No'),
    )
    patente=models.CharField('Patente',max_length=14, unique=True)
    color_vehiculo=models.CharField('Color Vehiculo',max_length=30)
    cant_puerta=models.IntegerField('Puertas',null=True)
    aire_acondicionado=models.CharField('Color Vehiculo',max_length=30, choices=AIRE_CHOICES)
    cant_asiento=models.IntegerField('Asiento',null=True)
    disponibilidad_vehi=models.CharField('Color Vehiculo',max_length=30, choices=DISPONIBILIDADVEHICULO_CHOICES)
    imagen_vehiculo = models.ImageField( default="", blank=True, null=True)
    modelo=models.CharField(max_length=30, default="")
    marca=models.CharField(max_length=30, default="")

    def __str__ (self):
        return self.patente  

class Conductor(models.Model):
    cond_rut=models.CharField('Rut',max_length=14, unique=True)
    cond_nombre=models.CharField('Nombre',max_length=30)
    cond_apellidos=models.CharField('Apellidos',max_length=30)
    cond_edad= models.IntegerField('Edad')
    cond_nacionalidad=models.CharField('Nacionalidad',max_length=30)
    cond_email= models.EmailField('Correo',blank=True)
    cond_telefono=models.CharField('Telefono',max_length=12)
    vehiculo=models.ManyToManyField(Vehiculo)

    def __str__ (self):
        return self.cond_nombre

class Tour(models.Model):
    
    CATEGORIATOUR_CHOICES = (
        ('Tour City', 'Tour City'),
        ('Turismo Aventura', 'Turismo Aventura'),
    )
    COMESTIBLE_CHOICES = (
        ('Si', 'Si'),
        ('No', 'No'),
    )
    descripcion_tour=models.CharField(max_length=100, default="")
    categoria=models.CharField(max_length=100, default="", choices=CATEGORIATOUR_CHOICES)
    comestible=models.CharField(max_length=100, default="", choices=COMESTIBLE_CHOICES)
    valor_tour=models.IntegerField('Valor', default='0')
    imagen_tour = models.ImageField( default="", blank=True, null=True)

    def __str__ (self):
        return self.categoria


class ServicioExtra(models.Model):
    descrip_servicio=models.CharField('Descripcion Servicios',max_length=20)
    direccion_reunion=models.CharField('Reunion',max_length=50)
    direccion_destino=models.CharField('Desatino',max_length=50)
    fecha_encuentro=models.DateField('Fecha encuentro')
    fecha_termino_servicio=models.DateField('Fecha Termino', default='')
    valor_servicio=models.IntegerField('Valor')
    conductor=models.ForeignKey(Conductor, on_delete=models.CASCADE, null=True, blank=True)
    tour=models.ForeignKey(Tour, on_delete=models.CASCADE, null=True, blank=True)

    def __str__ (self):
        return self.descrip_servicio      

class Reserva(models.Model):
    Codigo_Reserva = models.CharField(max_length=5, default = random_string, unique=True)
    Fecha_Reserva_Inicio = models.DateField(blank=True)   
    Fecha_Reserva_Termino = models.DateField(blank=True)
    Cantidad_Dias=models.IntegerField('Valor', default="0")
    Estado_Reserva = models.BooleanField(default=False)
    user=models.ForeignKey(User, on_delete=models.CASCADE, default="")
    departamento=models.ForeignKey(Departamento, on_delete=models.CASCADE, default="")
    servicioextra=models.ManyToManyField(ServicioExtra, null=True, blank=True)

    def __str__ (self):
        return self.Codigo_Reserva

class Contact(models.Model):
    asunto = models.CharField( max_length=50)
    descripcioncontacto = models.TextField()
    correoaenviar = models.EmailField(default="")

    def __str__(self):
        return self.asunto