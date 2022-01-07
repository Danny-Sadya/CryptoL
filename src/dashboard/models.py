from django.db import models

SORT_TYPES = (('asc', 'Ascending'),
              ('desc', 'Descending'),
              ('rar', 'Rarity'))


class SearchModel(models.Model):
    search_query = models.CharField(max_length=255, blank=True, null=True)
    sort_by = models.CharField(choices=SORT_TYPES, blank=True, null=True, max_length=255)
    max_price = models.IntegerField(null=True, blank=True)
    min_price = models.IntegerField(null=True, blank=True)
    is_auction = models.BooleanField(null=True, blank=True)
    is_buy_now = models.BooleanField(null=True, blank=True)
