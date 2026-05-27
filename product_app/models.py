from django.db import models


class Product(models.Model):

    p_name = models.CharField(max_length=200)

    p_type = models.CharField(max_length=200)

    p_price = models.FloatField()

    p_quantity = models.IntegerField()

    def __str__(self):

        return self.p_name


class Cart(models.Model):

    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)

    def __str__(self):

        return self.product.p_name