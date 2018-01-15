from django.db import models

# Create your models here.
class Compra(models.Model):
    provedor = models.CharField(max_length=250)
    produto = models.CharField(max_length=250)
    preco = models.FloatField(max_length=100)
    codigo = models.CharField(max_length=100)
    cliente = models.CharField(max_length=250)

    def __str__(self):
        return self.produto + ' - ' + self.codigo
