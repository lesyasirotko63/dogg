from django.test import TestCase
from catalog.models import Item, Order

import hashlib

class ItemModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        h1 = hashlib.sha1(('Big' + str(10000)).encode("utf-8"))
        Item.objects.create(item_id = h1.hexdigest(), name='Big', price=10000)

    def test_name_label(self):
        item = Item.objects.get(id=1)
        field_label = item._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        item = Item.objects.get(id=1)
        max_length = item._meta.get_field('name').max_length
        self.assertEqual(max_length, 20)

    def test_item_id_max_length(self):
        item = Item.objects.get(id=1)
        max_length = item._meta.get_field('item_id').max_length
        self.assertEqual(max_length, 32)

    def test_object_name_is_name(self):
        item = Item.objects.get(id=1)
        expected_object_name = f'{item.name}'
        self.assertEqual(expected_object_name, str(item))
