from django.test import TestCase
from db_service.models import User

# Create your tests here.
class ModelsTestCase(TestCase):	
    fixtures = ["models.json",]

    def test_user_from_fixture_exists(self):
        d1 = User.objects.get(firstname="Test", lastname="One")
        self.assertIsNotNone(d1)