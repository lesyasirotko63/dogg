from django.test import TestCase
from django.urls import reverse

from django.contrib.auth.models import User
from catalog.models import Order

class OrderPlaceTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user1.save()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/catalog/store')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('bulldog'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('akita'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'akita.html')

    def test_order_is_placed(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get('/catalog/place_order/Pincet')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('order_received' in response.context)
        self.assertTrue(response.context['order_received'] == True)
        self.assertTrue(response.context['item'] == 'Pincet')
