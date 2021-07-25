from django.test import TestCase, Client
from homepage.models import BlogPost, User

DEFAULT_USERNAME="TESTUSER"
DEFAULT_PASSWORD="Testing123!"

# Create your tests here.
class LoginCase(TestCase):
    def setUp(self):
        u = User.objects.create_user(username=DEFAULT_USERNAME, password=DEFAULT_PASSWORD)
        u.save()

    def test_user_created(self):
        identifier = "TEST_USER_CREATED"
        response = self.client.post('/register', {'username': DEFAULT_USERNAME+identifier, 'password': DEFAULT_PASSWORD})
        self.assertIs(response.status, 200)
        u = User.objects.get(username=DEFAULT_USERNAME+identifier)
        self.assertIsNotNone(u)

    def test_user_login(self):
        u = User.objects.get(username=DEFAULT_USERNAME)
        response = self.client.get('/login', {'username': DEFAULT_USERNAME, 'password': DEFAULT_PASSWORD})
        self.assertIs(response.status, 200)
        self.assertIs(response.request.user, u)

    def test_user_logout(self):
        u = User.objects.get(username=DEFAULT_USERNAME)
        response = self.client.get('/logout')
        self.assertIs(response.status, 200)
        self.assertIs(response.request.user.is_authenticated, True) 
