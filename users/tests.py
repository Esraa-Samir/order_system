from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from django.urls import reverse
from users.views import *


class ProductTests(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()


    def test_create_user(self):
        """
            Validate creating new user, (sign up functionality)
        """
        view = UserCreateView.as_view({'post': 'create'})
        uri = reverse('create-user')
        data = {
            "username": "TestUser",
            "email": "user@test.com",
            "password": 12345678
        }
        request = self.factory.post(uri, data)
        response = view(request)
        self.assertEqual(response.status_code, 201,
                         f'Expected Response Code 201, received {response.status_code} instead.')
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'TestUser')








