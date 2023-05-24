import random
import factory
from django.test import TestCase
from .models import User


class RandomUserFactory(factory.django.DjangoModelFactory):
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    age = random.randint(1, 100)

    class Meta:
        model = User


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = RandomUserFactory()

    def test_user_creation(self):
        self.assertTrue(isinstance(self.user, User))
        self.assertEqual(self.user.__str__(), f"{self.user.id}: {self.user.first_name} {self.user.last_name}")
        self.assertEqual(self.user.first_name, self.user.first_name)
        self.assertEqual(self.user.last_name, self.user.last_name)
        self.assertEqual(self.user.age, self.user.age)


class UserViewSetTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = RandomUserFactory.create()

    def test_user_create(self):
        user_data = {
            "id": 1,
            "first_name": "x",
            "last_name": "k",
            "age": 10
        }
        resp = self.client.post(f'/users/', data=user_data)
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.json().get('first_name'), user_data.get('first_name'))

    def test_get_user_detail(self):
        resp = self.client.get(f'/users/{self.user.id}/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json().get('first_name'), self.user.first_name)

    def test_delete_user(self):
        response = self.client.delete(f'/users/{self.user.id}/')
        print(self.user)
        print(response.request)
        self.assertEqual(response.status_code, 204)
