from django.test import TestCase, Client
from db_service.models import User, Event, Ticket, Purchase, Authenticator
import json
import time

# Create your tests here.
class ModelsTestCase(TestCase):
    fixtures = ["models.json",]
    def setUp(self):
        c = Client()
        create_response = c.post('/api/v1/create/user/', {
            "username": "jeffaccount",
            "firstname": "Jeff",
            "lastname": "Roberts",
            "password": "password"
        })
        validate_response = c.post('/api/v1/user/validate/', {
            "username": "jeffaccount",
            "password": "password"
        })
        v_dict = json.loads(validate_response.content)
        user_id = v_dict["resp"]["user_id"]
        auth_response = c.post('/api/v1/create/authenticator/', {
            "user_id": user_id
        })
        event_response = c.post('/api/v1/create/event/', {
            "name" : "Acapella Show #594",
            "description" : "Unnessecary",
            "location" : "105 McCleod Hall",
            "start_time" : "2015-12-25 09:19:30.108740+03:00",
            "creator_id" : user_id
        })

    def test_user_from_fixture_exists(self):
        u1 = User.objects.get(firstname="Test", lastname="One")
        self.assertEqual(u1.username, "testuser1")

    def test_user_from_setup_exists(self):
        u2 = User.objects.get(firstname="Jeff", lastname="Roberts")
        self.assertEqual(u2.username, "jeffaccount")

    def test_tests_are_actually_working(self):
        t1 = User.objects.get(firstname="Jeff", lastname="Roberts")
        self.assertNotEqual(t1.username, "asdasdqwe1")

    def test_event_from_fixture_exists(self):
        e1 = Event.objects.get(name="testevent1")
        self.assertEqual(e1.description, "desc")

    def test_ticket_from_fixture_exists(self):
        e1 = Ticket.objects.get(id="1")
        self.assertEqual(e1.price, 4.0)

    def test_bad_ticket(self):
        e1 = Ticket.objects.get(id="1")
        self.assertNotEqual(e1.price, 4.1)

    def test_purchase_from_fixture_exists(self):
        e1 = Purchase.objects.get(id="1")
        e2 = Ticket.objects.get(id="1")
        self.assertEqual(e1.ticket, e2)

    def test_auth_from_fixture_exists(self):
        e1 = Authenticator.objects.get(authenticator=1)
        self.assertEqual(e1.user_id, 1)

    def test_auth_user_setup_exists(self):
        u1 = User.objects.get(username="jeffaccount")
        e1 = Authenticator.objects.get(user_id=u1.id)

