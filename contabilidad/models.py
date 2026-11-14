from django.db import models

# Create your models here.


class Cuenta(models.Model):
    #tipo de cuentas contables fijas
    TIPO_CUENTA_CHOISE = [
        ('ACTIVO', 'activo'),
        ('PASIVO', 'pasivo'),
        ('PATRIMONIO', 'patrimonio'),
        ('INGRESO', 'ingreso'),
        ('GASTO','gasto'),
        ('COSTO', 'costo')
    ]

    #codigo de cuenta
    codigo = models.CharField(max_length=30, unique=True, verbose_name="Codigo de la cuenta") #varchar
    #nombre de cuenta
    nombre =  models.CharField(max_length=200, verbose_name="Nombre de la cuenta")
    #tipo de cuenta
    tipo = models.CharField(max_length=20, choices=TIPO_CUENTA_CHOISE, verbose_name="Tipo de cuenta")

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

class Partida(models.Model):
    numero_comprobante = models.CharField(max_length=30, unique=True, verbose_name="Numero de comprobante")
    fecha = models.DateField(verbose_name="Fecha de la partida")
    descripcion = models.CharField(max_length=200, verbose_name="Descripcion de la partida")

    def __str__(self):
        return f"Partida : {self.numero_comprobante} - {self.fecha}"



class DetallePartida(models.Model):
    #conexion a Partida, on_delete =  models.CASCADE si se borra una partida se borra su detalle correspodiente
    partida = models.ForeignKey(Partida, on_delete=models.CASCADE, related_name="detalles")

    #conexion a Cuenta. on_delete = models.PROTECT para evitar borrar una cuenta si ya tiene partidas asociadas
    cuenta = models.ForeignKey(Cuenta, on_delete=models.PROTECT, related_name="detalles")

    # CUENTA T
    # Debe(Cargo) y Haber(Abono)
    debe = models.DecimalField(max_digits=12, decimal_places=2, default=0.00, verbose_name="Debe (Cargo)")
    haber = models.DecimalField(max_digits=12, decimal_places=2, default=0.00, verbose_name="Haber (Abono)")

    def __str__(self):
        return f"{self.cuenta.nombre} | Debe: {self.debe} | Haber: {self.haber}"
