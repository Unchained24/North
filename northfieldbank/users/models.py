from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Reg(models.Model):
    user = models.OneToOneField(User, null=True, on_delete= models.CASCADE)
    account_no = models.CharField(max_length=50, null='TRUE')
    firstname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_no = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state= models.CharField(max_length=50)
    country= models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    job= models.CharField(max_length=50)

    account_balance = models.CharField(max_length=50)
    account_pin = models.CharField(max_length=50)
    
    dp = models.ImageField(null=True , blank=True, default="default.jpg", upload_to="ItemImage")
    status = models.CharField(max_length=50)    

    def __str__(self):
        return self.account_no