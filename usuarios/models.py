# Create your models here.

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Usuario(AbstractUser):
    nombres = models.CharField(max_length=100, blank=True)
    apellidos = models.CharField(max_length=100, blank=True)
    edad = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(unique=True)

    # Evitar conflictos de reverse accessors
    groups = models.ManyToManyField(
        Group,
        related_name='usuarios_set',  # aquí cambia el related_name
        blank=True,
        help_text='Grupos a los que pertenece este usuario.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='usuarios_user_set',  # aquí cambia el related_name
        blank=True,
        help_text='Permisos específicos para este usuario.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username