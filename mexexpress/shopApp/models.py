from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100,unique=True)
    product_description = models.CharField(max_length=255)
    product_full_cost = models.DecimalField(max_digits=8,decimal_places=2)
    product_is_offer = models.BooleanField()
    product_offer_cost = models.DecimalField(max_digits=8,decimal_places=2)

    def __str__(self):
        return self.product_name

class HistoricalCost(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    chance_date = models.DateTimeField()
    product_cost = models.DecimalField(max_digits=8,decimal_places=2)
    product_is_offer = models.BooleanField()

    def __str__(self):
        return self.product.product_name + " " + self.chance_date.strftime('%Y-%m-%d %H:%M')


class Contacts(models.Model):
    contact_full_name = models.CharField(max_length=255)
    contact_address = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=15)
    contact_email = models.EmailField(max_length=150,default='alex@gmail.com')
    contact_activate = models.BooleanField()

    def __str__(self):
        return self.contact_full_name
