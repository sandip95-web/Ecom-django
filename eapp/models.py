from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Product(models.Model):
    product_name=models.CharField(max_length=100)
    price=models.IntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    description=models.TextField(max_length=200,default='',blank=True)
    image=models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.product_name
    
class Customer_account(models.Model):
    full_name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    mobile_number=models.CharField(max_length=10,default='')
    def __str__(self):
        return self.full_name
    
class Cart(models.Model):
    phone=models.CharField(max_length=10)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    image=models.ImageField(null=True,blank=True)
    quantity=models.PositiveIntegerField(default=1)
    price=models.IntegerField(default=0)
    total=models.IntegerField(default=0)
    
class Contact(models.Model):
    full_name=models.CharField(max_length=20)
    email=models.EmailField()
    mobile=models.IntegerField()
    message=models.TextField()
    
    def __str__(self):
        return self.full_name
    
    
    
