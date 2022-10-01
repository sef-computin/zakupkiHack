from django.db import models

# Create your models here.
class Contracts(models.Model):

    product_name = models.TextField(blank=True, primary_key=True)
    price = models.FloatField(blank=True, null=True)
    product_vat_rate = models.TextField(blank=True, null=True)
    product_msr = models.TextField(blank=True, null=True)
    product_characteristics = models.TextField(blank=True, null=True)
    okpd2_code = models.TextField(blank=True, null=True)
    okpd2_name = models.TextField(blank=True, null=True)
    inn = models.TextField(blank=True, null=True)
    country_code = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Contract'
        verbose_name_plural = 'Contracts'
        managed = False
        db_table = 'Contracts'

