from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from usuarios.forms import CustomPasswordResetForm

urlpatterns = [
    #agregar urls para usuarios
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/', views.perfil_view, name='perfil'),


    # 1. Pantalla para pedir el correo
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="usuarios/password_reset.html", form_class= CustomPasswordResetForm), name="password_reset"),
    
    # 2. Pantalla de confirmacion de envio
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="usuarios/password_reset_sent.html"), name="password_reset_done"),
    
    # 3. Enlace que viene en el correo para ingresar nueva contraseña
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="usuarios/password_reset_form.html"), name="password_reset_confirm"),
    
    # 4. Pantalla de exito final
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="usuarios/password_reset_done.html"), name="password_reset_complete"),
]