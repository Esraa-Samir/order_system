from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from purchases.views import *
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token


class PurchaseTests(APITestCase):

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

        self.purchases = [Purchase.objects.create(item=self.product, purchaser=self.user['user']),
                          Purchase.objects.create(item=self.product, purchaser=self.user['user']),
                          Purchase.objects.create(item=self.product, purchaser=self.user['admin']),
                          Purchase.objects.create(item=self.product, purchaser =self.user['admin']),]

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

    def test_purchase_product(self):
        """
            Validate purchasing a product.
        """
        view = PurchaseProductView.as_view({'post': 'create'})
        uri = reverse('purchases:create-purchase')
        data = {
            "item": self.product_id,
        }
        request = self.factory.post(uri, data, HTTP_AUTHORIZATION='Token {}'.format(self.token_user.key))
        request.user = self.user['user']
        response = view(request)
        self.assertEqual(response.status_code, 201,
                         f'Expected Response Code 201, received {response.status_code} instead.')
        self.assertEqual(Purchase.objects.count(), len(self.purchases) + 1)


    def test_purchase_product_by_owner(self):
        """
            Validate that a product owner can not purchase it.
        """
        view = PurchaseProductView.as_view({'post': 'create'})
        uri = reverse('purchases:create-purchase')
        data = {
            "item": self.product_id,
        }
        request = self.factory.post(uri, data, HTTP_AUTHORIZATION='Token {}'.format(self.token_admin.key))
        request.user = self.user['admin']
        response = view(request)
        self.assertEqual(response.status_code, 403,
                         f'Expected Response Code 403, received {response.status_code} instead.')

    def test_list_user_purchases(self):
        """
            Validate listing users' purchases.
        """
        view = PurchaseListView.as_view({'get': 'list'})
        uri = reverse('purchases:list-purchases')
        request = self.factory.get(uri, HTTP_AUTHORIZATION='Token {}'.format(self.token_user.key))
        request.user = self.user['user']
        response = view(request)
        self.assertEqual(response.status_code, 200,
                         f'Expected Response Code 200, received {response.status_code} instead.')
        # self.assertEqual(response.data)

    def test_get_Revenue_admin(self):
        """
            Validate that an admin can view Revenue.
        """
        view = PurchaseRevenueView.as_view({'get': 'list'})
        uri = reverse('purchases:get-Revenue')
        request = self.factory.get(uri, HTTP_AUTHORIZATION='Token {}'.format(self.token_admin.key))
        request.user = self.user['admin']
        response = view(request)
        self.assertEqual(response.status_code, 200,
                         f'Expected Response Code 200, received {response.status_code} instead.')

    def test_get_Revenue_normal_user(self):
        """
            Validate that a normal user can not view Revenue.
        """
        view = PurchaseRevenueView.as_view({'get': 'list'})
        uri = reverse('purchases:get-Revenue')
        request = self.factory.get(uri, HTTP_AUTHORIZATION='Token {}'.format(self.token_user.key))
        request.user = self.user['user']
        response = view(request)
        self.assertEqual(response.status_code, 403,
                         f'Expected Response Code 403, received {response.status_code} instead.')
