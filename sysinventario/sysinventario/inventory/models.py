from django.db import models
from datetime import datetime
# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.CharField(max_length=150, verbose_name='Descripcion')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Products(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    categoria_id = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos' 
