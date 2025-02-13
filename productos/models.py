from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.URLField()

    def __str__(self):
        return self.nombre, self.precio, self.imagen

    #Necesito una función que devuelva el objeto en forma de dict

    def to_dict(self):
        return {
            #'clave':'valor'

            'nombre':self.nombre,
            'precio':self.precio,
            'imagen':self.imagen
        }