from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    # Campos que se mostrarán en la lista general de usuarios
    list_display = ('username', 'email', 'nombres', 'apellidos', 'edad', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    
    # Secciones que se mostrarán al editar un usuario existente
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información personal', {'fields': ('nombres', 'apellidos', 'edad', 'email')}),
        ('Permisos', {'fields': ('is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )
    
    # Campos que se pedirán al crear un usuario nuevo desde el admin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'nombres', 'apellidos', 'edad', 'password1', 'password2', 'is_staff', 'is_active')
        }),
    )
    
    search_fields = ('username', 'email', 'nombres', 'apellidos')
    ordering = ('username',)

admin.site.register(Usuario, UsuarioAdmin)