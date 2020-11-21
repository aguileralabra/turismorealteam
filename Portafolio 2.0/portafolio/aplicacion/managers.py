from django.db import models
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager, models.Manager):
    
    def _create_user(self, username, cli_Rut, password, is_staff, is_superuser, is_active,**extra_fields):
        user = self.model(
            username=username,
            cli_Rut=cli_Rut,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_user(self, username, cli_Rut, password=None, **extra_fields):
        return self._create_user(username, cli_Rut, password, False, False, False, **extra_fields )

    def create_superuser(self, username, cli_Rut, password=None, **extra_fields):
        return self._create_user(username, cli_Rut, password, True, True, True, **extra_fields )

    def cod_validation(self, id_user, cod_registro):
        if self.filter(id=id_user, codregistro=cod_registro).exists():
            return True
        else:
            return False

class AgregarReservaManager(models.Manager):
    def total_cobrar(self):
        consulta = self.aggregate(
            total=Sum(
                F('Cantidad_Dias')*F('Reserva_departamento_valor_servicio'),
                output_field=FloatField()
            ),
        )
        if consulta['total']:
            return consulta['total']
        else:
            return 0

