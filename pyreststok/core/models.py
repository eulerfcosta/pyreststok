from django.contrib.auth.models import User, Group
from django.db import models


# Create your models here.

class Client(models.Model) :
    name = models.CharField(max_length=200,  blank=False, null=False)
    doc = models.CharField(max_length=25 , blank=False, null=False)
    is_stok = models.BooleanField(null=False,default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


    class Meta:
        managed = True
        db_table = 'clients'

class Stok_Type(models.Model) :
    name = models.CharField(max_length=200,  blank=False, null=False , unique = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


    class Meta:
        managed = True
        db_table = 'stoks_types'

class Product_Type(models.Model) :
    name = models.CharField(max_length=200,  blank=False, null=False , unique = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


    class Meta:
        managed = True
        db_table = 'products_types'


class Condominium(models.Model) :
    name = models.CharField(max_length = 200,  blank = False, null = False )
    address = models.CharField(max_length = 200, blank = False, null = False)
    number = models.CharField(max_length = 7,  blank = True, null = True)
    complement = models.CharField(max_length = 200, blank = True, null = True)
    neighborhood = models.CharField(max_length = 200, blank = False, null = True)
    zipcode = models.CharField(max_length = 8, blank = False, null = False)
    city = models.CharField(max_length = 200, blank = False, null = False)
    state = models.CharField(max_length=2, blank = False, null = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name


    class Meta:
        managed = True
        db_table = 'condominiums'

class Client_Address(models.Model) :
    is_codominium= models.BooleanField(default= False, null = False)
    condominium = models.ForeignKey('Condominium' , models.DO_NOTHING)
    client = models.ForeignKey('Client', models.DO_NOTHING)
    address = models.CharField(max_length = 200, blank = False, null = False)
    number = models.CharField(max_length = 7,  blank = True, null = True)
    complement = models.CharField(max_length = 200, blank = True, null = True)
    neighborhood = models.CharField(max_length = 200, blank = False, null = True)
    zipcode = models.CharField(max_length = 8, blank = False, null = False)
    city = models.CharField(max_length = 200, blank = False, null = False)
    state = models.CharField(max_length=2, blank = False, null = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client.name


    class Meta:
        managed = True
        db_table = 'clients_addresses'


class Product(models.Model):
    name = models.CharField(max_length = 200, blank = False, null = False, unique = True)
    product_type = models.ForeignKey('Product_type', models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'products'


class Stok(models.Model):
    name = models.CharField(max_length = 200, blank = False, null = False, unique = True)
    stok_type = models.ForeignKey('Stok_type', models.DO_NOTHING)
    client  = models.ForeignKey('Client', models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'stoks'

class Item(models.Model):
    product = models.ForeignKey('Product', models.DO_NOTHING)
    stok = models.ForeignKey('Stok', models.DO_NOTHING)
    user = models.ForeignKey(User, models.DO_NOTHING)
    sn = models.CharField(max_length = 200, null = False , blank = False , unique = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        name = self.product.name + self.sn
        return self.name

    class Meta:
        managed = True
        db_table = 'items'

class Stok_Moviment(models.Model):
    item = models.ForeignKey('Item', models.DO_NOTHING)
    stok = models.ForeignKey('Stok', models.DO_NOTHING)
    user = models.ForeignKey(User, models.DO_NOTHING)
    is_active = models.BooleanField(default = True, null = False, blank = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        name = self.item.product.name + ' - ' + self.item.sn
        return name

    class Meta:
        managed = True
        db_table = 'stoks_moviments'
