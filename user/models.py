from django.db import models

# Create your models here.
class User(models.Model):
    u_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100,null=True)
    full_name = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=40,null=True)
    password = models.CharField(max_length=100,null=True)
    confirm_password = models.CharField(max_length=100,null=True)
    class Meta:
        db_table = "user"

class Seller(models.Model):
    sc = models.CharField(max_length=50,null=True)
    simg = models.ImageField(upload_to="seller", blank=True, null=True)
    ain = models.CharField(max_length=100,null=True)
    aip = models.CharField(max_length=100,null=True)
    aid = models.CharField(max_length=250,null=True)
    st = models.CharField(max_length=50,null=True)
    et = models.CharField(max_length=50,null=True)
    fn = models.CharField(max_length=50,null=True)
    em = models.CharField(max_length=50,null=True)
    ph = models.CharField(max_length=50,null=True)
    bd = models.CharField(max_length=50,null=True)
    gen = models.CharField(max_length=50,null=True)
    street = models.CharField(max_length=250,null=True)
    lnk = models.CharField(max_length=100,null=True)
    cty = models.CharField(max_length=100,null=True)
    stat = models.CharField(max_length=50,null=True)
    pin = models.CharField(max_length=20,null=True)
    aadh = models.CharField(max_length=30,null=True)
    pan = models.CharField(max_length=10,null=True)
    UPI = models.CharField(max_length=35,null=True)
    bank = models.CharField(max_length=30,null=True)
    POA = models.CharField(max_length=30,null=True)
    class Meta:
        db_table = "seller"

class Bidder(models.Model):
    b_id = models.AutoField(primary_key=True)
    bfn = models.CharField(max_length=50,null=True)
    bem = models.CharField(max_length=50,null=True)
    bph = models.CharField(max_length=50,null=True)
    bbd = models.CharField(max_length=50,null=True)
    bgen = models.CharField(max_length=50,null=True)
    bstreet = models.CharField(max_length=250,null=True)
    blnk = models.CharField(max_length=100,null=True)
    bcty = models.CharField(max_length=100,null=True)
    bstat = models.CharField(max_length=50,null=True)
    bpin = models.CharField(max_length=20,null=True)
    baadh = models.CharField(max_length=30,null=True)
    bpan = models.CharField(max_length=10,null=True)
    bUPI = models.CharField(max_length=35,null=True)
    bbank = models.CharField(max_length=30,null=True)
    class Meta:
        db_table = "bidder"