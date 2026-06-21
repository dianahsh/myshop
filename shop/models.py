from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, 
                                on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200)
    # color
    image = models.ImageField(upload_to="images", blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12,decimal_places=2)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    payment = models.BooleanField(default=False)
    date = models.DateField(auto_now=True)
    address = models.CharField(max_length=250)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return str(self.id)
    
class OrderList(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orders_list')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders_list')
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=12,decimal_places=2)

    def __str__(self):
        return str(self.id)
    
class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')

class ShoppinList(models.Model):
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, related_name='shoppings_list')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='shoppings_list')
    quantity = models.IntegerField(default=1)

class review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reveiws')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reveiws')
    date = models.DateField(auto_now=True)


    