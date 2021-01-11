from django.db import models
from django.contrib.auth.models import User
import hashlib

# Create your models here.

class Item(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    item_id = models.CharField(max_length=32, help_text='Enter field documentation')
    name = models.CharField(max_length=20, help_text='Enter field documentation')
    price = models.CharField(max_length=20, help_text='Enter field documentation')
    ...

    # Metadata
    class Meta:
        ordering = ['name']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.item_id)])

    def __str__(self):
        """String for representing the Item object (in Admin site etc.)."""
        return self.name

class Order(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    order_id = models.CharField(max_length=32, help_text='Enter field documentation')
    date = models.DateTimeField(max_length=20, help_text='Enter field documentation', auto_now_add=True)
    customer = models.ForeignKey(User, verbose_name='customer', related_name='order_to_customer', null=True, on_delete=models.SET_NULL)
    item = models.ForeignKey(Item, related_name='order_to_item', verbose_name='item', on_delete=models.RESTRICT)
    ...

    # Metadata
    class Meta:
        ordering = ['-date']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.order_id)])

    def __str__(self):
        """String for representing the Order object (in Admin site etc.)."""
        return (self.order_id + ' ' + str(self.date))