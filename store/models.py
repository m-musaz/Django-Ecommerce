from django.db import models

# Create your models here.


class Collection(models.Model):
    title = models.CharField(max_length=255,null=True)
    featured_product = models.ForeignKey('Product',on_delete=models.SET_NULL,null=True,related_name='+')

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Product(models.Model):
    title = models.CharField(max_length=255,null=True)
    slug = models.SlugField(default='-')
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2,null=True)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection,on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2,null=True)

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

    class Meta:
        db_table = 'store_customers'
        indexes = [
            models.Index(fields=['first_name','last_name'])
        ]

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
    title = models.CharField(max_length=255,null=True)
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
    product = models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6,decimal_places=2,null=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    Product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    Customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    zip = models.CharField(max_length=255,default='-')
