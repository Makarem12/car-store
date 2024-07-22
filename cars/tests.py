from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Car

class CarsTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test_user',
            email='test@email.com',
            password='1234'
        )

        self.car = Car.objects.create(
            buyer_id=self.user,
            model='test_model',
            brand='test_brand',
            price=1.1,
            is_bought=False
        )

    def test_list_page_status_code(self):
        url = reverse('cars_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse('cars_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'cars_list.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_str_method(self):
     self.assertEqual(str(self.car), 'test_brand test_model')


    def test_details_view(self):
        url = reverse('car_details', args=[self.car.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'car_details.html')

    def test_create_view(self):
        obj = {
            'buyer_id': self.user.id,
            'model': 'test_model',
            'brand': 'test_brand',
            'price': 1.1,
            'is_bought': False
        }

        url = reverse('create_car')
        response = self.client.post(path=url, data=obj, follow=True)
        self.assertEqual(len(Car.objects.all()), 2)
        self.assertRedirects(response, reverse('car_details', args=[2]))
