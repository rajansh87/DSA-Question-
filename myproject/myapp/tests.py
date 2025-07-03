from django.test import TestCase

# Create your tests here.
from .models import User,Apartment
from .views import *

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(name="John Doe", userId=1)
        User.objects.create(name="Jane Smith", userId=2)

    def test_user_creation(self):
        john = User.objects.get(userId=1)
        jane = User.objects.get(userId=2)
        self.assertEqual(john.name, "John Doe")
        self.assertEqual(jane.name, "Jane Smith")

if __name__ == '__main__':
    views