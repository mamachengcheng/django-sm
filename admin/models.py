from __future__ import unicode_literals

from django.db import models


class Order(models.Model):
    order_id = models.CharField(max_length=30)
    order_date = models.DateField(auto_now_add=True)
    customer_name = models.CharField(max_length=8)
    phone_case_pattern = models.ImageField()
    phone_type = models.CharField(max_length=13)
    address = models.CharField(max_length=80)
    is_handle = models.BooleanField(default=False)

    class Meta:
        db_table = "order"
