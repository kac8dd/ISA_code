from django.test import TestCase, Client
import json
import time

# Create your tests here.
class ExpTestCase(TestCase):
    def setUp(self):
    	pass

    # NameError: name 'this' is not defined
    # I have not been able to understand how this can break 
    # while the models tests, which use the same base class/format, work
    def test_sanity(self):
        this.assertEqual(1, 1)

#
#    def test_integration(self):
#        c = Client()
#        #returns authenticator
#        create_response = c.post('/api/v1/user/create/', {
#            "username": "jeffaccount",
#            "firstname": "Jeff",
#            "lastname": "Roberts",
#            "passwordd": "password"
#        })
#        c_dict = json.loads(create_response.content)
#        auth = c_dict["resp"]["authenticator"]
#        logout_response = c.post('/api/v1/user/logout/', {
#            "authenticator": auth,
#        })
#        l_dict = json.loads(logout_response.content)
#        user_id = l_dict["resp"]["user_id"]
#        login_response = c.post('/api/v1/user/login/', {
#            "username": "jeffaccount",
#            "firstname": "Jeff"        	
#        })
#        l_dict = json.loads(login_response.content)
#        auth2 = l_dict["resp"]["authenticator"]