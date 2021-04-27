from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from products.views import *
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from djmoney.money import Money


class ProductTests(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = self.setup_user()
        self.token_admin = Token.objects.create(user=self.user['admin'])
        self.token_admin.save()
        self.token_user = Token.objects.create(user=self.user['user'])
        self.token_user.save()
        self.product = Product.objects.create(name='Headphones', description='electronics', price=600,
                                              owner=self.user['admin'],
                                              is_available=True)
        self.product_id = self.product.id

    @staticmethod
    def setup_user():
        User = get_user_model()
        return {'admin': User.objects.create_user(
            'Admin',
            email='Admin@test.com',
            password='Admin',
            is_admin=True
        ),
            'user': User.objects.create_user(
                'User',
                email='User@test.com',
                password='User',
                is_admin=False
            )
        }

    def test_list_products(self):
        """
           check product listing.
        """
        view = ProductCreateListView.as_view({'get': 'list'})
        uri = reverse('products:create/list-products')
        request = self.factory.get(uri, HTTP_AUTHORIZATION='Token {}'.format(self.token_admin.key))
        request.user = self.user['admin']
        response = view(request)
        self.assertEqual(response.status_code, 200,
                         f'Expected Response Code 200, received {response.status_code} instead.')

    def test_add_product(self):
        """
            validate adding new product.
        """
        view = ProductCreateListView.as_view({'post': 'create'})
        uri = reverse('products:create/list-products')
        data = {
            "name": "Iphone 7",
            "description": "Mobile phone",
            "price": 200,
            "is_available": True
        }
        request = self.factory.post(uri, data, HTTP_AUTHORIZATION='Token {}'.format(self.token_admin.key))
        request.user = self.user['admin']
        response = view(request)
        self.assertEqual(response.status_code, 201,
                         f'Expected Response Code 201, received {response.status_code} instead.')

    # def test_partial_update_product(self):
    #     view = ProductUpdateView.as_view({'patch': 'update'})
    #     uri = reverse('products:update-product', kwargs={'pk': self.product_id})
    #     data = {
    #         "id": self.product_id,
    #         "is_available": False
    #     }
    #     request = self.factory.patch(uri, data, HTTP_AUTHORIZATION='Token {}'.format(self.token_admin.key))
    #     request.user = self.user['admin']
    #     response = view(request, pk=self.product_id)
    #     self.assertEqual(response.status_code, 200,
    #                      f'Expected Response Code 200, received {response.status_code} instead.')
    #     self.assertEqual(response.data['is_available'], data["is_available"])

    def test_full_update_product(self):
        """
            validate updating an existing product.
        """
        view = ProductUpdateView.as_view({'patch': 'update'})
        uri = reverse('products:update-product', kwargs={'pk': self.product_id})
        data = {
            "id": self.product_id,
            "name": "Headphone updated",
            "description": "New version",
            "price": "800",
            "price_currency": "USD",
            "is_available": True
        }
        request = self.factory.patch(uri, data, HTTP_AUTHORIZATION='Token {}'.format(self.token_admin.key))
        request.user = self.user['admin']
        response = view(request, pk=self.product_id)
        self.assertEqual(response.status_code, 200,
                         f'Expected Response Code 200, received {response.status_code} instead.')
        data['price'] = float(data['price'])
        response.data['price'] = float(response.data['price'])
        self.assertEqual(response.data, data)

    def test_delete_product(self):
        """
            validate deleting an existing product.
        """
        view = ProductDeleteView.as_view({'delete': 'destroy'})
        uri = reverse('products:delete-product', kwargs={'pk': self.product_id})
        request = self.factory.delete(uri, HTTP_AUTHORIZATION='Token {}'.format(self.token_admin.key))
        request.user = self.user['admin']
        response = view(request, pk=self.product_id)
        self.assertEqual(response.status_code, 204,
                         f'Expected Response Code 204, received {response.status_code} instead.')

    def test_list_available_product(self):
        """
            check available products listing.
        """
        view = AvailableProductListView.as_view({'get': 'list'})
        uri = reverse('products:list-available-products')
        request = self.factory.get(uri, HTTP_AUTHORIZATION='Token {}'.format(self.token_user.key))
        request.user = self.user['user']
        response = view(request)
        self.assertEqual(response.status_code, 200,
                         f'Expected Response Code 200, received {response.status_code} instead.')
