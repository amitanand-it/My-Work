from django.db import models

# Create your models here.
class Vendor(models.Model):
    company_name = models.CharField(max_length=30)
    contact_person = models.CharField(max_length=30)
    email = models.EmailField(max_length=255, null=False)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

class Item(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    starting_bid = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class VendorsBid(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    bid_amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class VendorLogins(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    username = models.EmailField(max_length=255) 
    password = models.CharField(max_length=30) 
    created_at = models.DateTimeField(auto_now_add=True)
class BidAllotment(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    bid_amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)