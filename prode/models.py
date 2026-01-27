from django.db import models 
from django.contrib.auth.models import AbstractUser

class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    dt = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Partido(models.Model):
    equipo_local = models.ForeignKey(Equipo, on_delete=models.PROTECT, related_name='partidos_locales')
    equipo_visitante = models.ForeignKey(Equipo, on_delete=models.PROTECT, related_name='partidos_visitantes')
    fecha = models.DateField()
    jugado = models.BooleanField(default=False)
    hora = models.TimeField(default='00:00:00')  # Agrega este campo con default
    def __str__(self):
        return f"{self.equipo_local} vs {self.equipo_visitante} en {self.fecha}"
    
class Pronostico(models.Model):
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE)
    goles_visitante = models.IntegerField(null=True, blank=True)
    goles_local = models.IntegerField(null=True, blank=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)

    def __str__(self):
        return f"Pronóstico para {self.partido}: {self.goles_local} - {self.goles_visitante} por {self.usuario.username}"
    
    class Meta:
     unique_together = [['usuario', 'partido']]


class Usuario(AbstractUser):
    puntos_prode = models.IntegerField(default=0)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuario_groups',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuario_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def CalcularPuntos(self):
        pass