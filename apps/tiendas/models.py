from django.db import models


# Create your models here.

class Tienda(models.Model):

    ESTATUS = (
        (1, "Activo"),
        (2, "Inactivo"),
        (3, "Suspendido"),
    )
    nombre = models.CharField(max_length=50)
    direccion = models.TextField()
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    estatus = models.IntegerField(choices=ESTATUS)

    class Meta:
        db_table = 'tiendas'
        ordering=['id']
