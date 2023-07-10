from django.test import TestCase, Client
from django.contrib.auth.models import User

class UserLoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)
    
    def test_user_login_success(self):
        response = self.client.post('/login/', {'username': self.username, 'password': self.password})
        self.assertEqual(response.status_code, 302)  # Verifica se o redirecionamento ocorreu
        self.assertEqual(response.url, '/home/')  # Verifica se o redirecionamento foi para a página correta
    
    def test_user_login_failure(self):
        response = self.client.post('/login/', {'username': 'invaliduser', 'password': 'invalidpassword'})
        self.assertEqual(response.status_code, 302)  # Verifica se o redirecionamento ocorreu
        self.assertEqual(response.url, '/login/')  # Verifica se o redirecionamento foi para a página correta
        self.assertContains(response, 'Usuário e/ou senha inválidos')  # Verifica se a mensagem de erro foi exibida

class UserLogoutTestCase(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_user_logout(self):
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 302)  # Verifica se o redirecionamento ocorreu
        self.assertEqual(response.url, '/login/')  # Verifica se o redirecionamento foi para a página correta

class CadastroTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = 'testuser'
        self.password = 'testpassword'
        self.email = 'test@example.com'
    
    def test_cadastro_success(self):
        response = self.client.post('/cadastro/', {'username': self.username, 'password': self.password, 're-password': self.password, 'email': self.email})
        self.assertEqual(response.status_code, 302)  # Verifica se o redirecionamento ocorreu
        self.assertEqual(response.url, '/login/')  # Verifica se o redirecionamento foi para a página correta
        user = User.objects.get(username=self.username)
        self.assertEqual(user.email, self.email)  # Verifica se o usuário foi criado corretamente
    
    def test_cadastro_failure(self):
        response = self.client.post('/cadastro/', {'username': self.username, 'password': self.password, 're-password': 'differentpassword', 'email': self.email})
        self.assertEqual(response.status_code, 200)  # Verifica se a página de cadastro foi renderizada novamente
        self.assertContains(response, 'Os campos de senha não correspondem')  # Verifica se a mensagem de erro foi exibida

