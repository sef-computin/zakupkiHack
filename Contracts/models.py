from django.db import models
from searchfuncs import Search

# Create your models here.

class SearchHandler():
    dictionary, index, tfidf = Search.init()
    print('[DEBUG] init static class')

    @classmethod
    def search(self, searchWord):
        ids = []
        ids = Search.search(self.dictionary, self.index, self.tfidf, searchWord)
        print('[DEBUG] search successful')
        return ids
        # Search.search(searchWord)

class Contracts(models.Model):

    id = models.IntegerField(blank=True, primary_key=True)
    product_id = models.IntegerField(blank=True, null=True)
    product_name = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    product_vat_rate = models.TextField(blank=True, null=True)
    product_msr = models.TextField(blank=True, null=True)
    product_characteristics = models.TextField(blank=True, null=True)
    okpd2_code = models.TextField(blank=True, null=True)
    okpd2_name = models.TextField(blank=True, null=True)
    inn = models.TextField(blank=True, null=True)
    country_code = models.IntegerField(blank=True, null=True)
    country_name = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Contract'
        verbose_name_plural = 'Contracts'
        managed = False
        db_table = 'Contracts'

