from __future__ import unicode_literals
from django.db import models

class Buyer(models.Model):
    buyer_name = models.CharField(max_length = 25)
    street_address = models.CharField(max_length = 20)
    zip_code = models.CharField(max_length = 20)
    city = models.CharField(max_length = 20)
    state = models.CharField(max_length = 20)
    class Meta:
        db_table = "buyer"

# Create your models here.
