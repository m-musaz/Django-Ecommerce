from django.db import models

# Create your models here.


class Collection(models.Model):
    title = models.CharField(max_length=255)

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection,on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)

class Cart(models.Model):
    item_name = models.Ma

class Customer(models.Model):
    MEMBERSHIP_VALUES=[
        ('B',"Bronze"),
        ('S',"Silver"),
        ('G',"Gold"),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone  = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)

    membership = models.CharField(max_length=1,choices=MEMBERSHIP_VALUES,default='B')

class Order(models.Model):
    PAYMENT_STATUS_VALUES=[
        ('P',"Pending"),
        ('C',"Complete"),
        ('F',"Failed"),
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1,choices=PAYMENT_STATUS_VALUES,default='P')
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    

class OrderItem(models.Model):
    title = models.CharField(max_length=255)
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
    product = models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6,decimal_places=2)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    Product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    Customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
