from django.db import models

class Product(models.Model):
    product_name = models.CharField('Наименование продукта', max_length=25)
    price = models.PositiveIntegerField('Цена за единицу товара')

    def __str__(self):
        return self.product_name

class Storage(models.Model):
    product = models.ForeignKey(Product, verbose_name='Продукт на складе', on_delete=models.CASCADE)
    stock = models.PositiveIntegerField('Запас на складе')
