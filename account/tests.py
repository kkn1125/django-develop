from django.test import Client, TestCase
from django.urls import reverse
from .models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your tests here.
class TestClient(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.c = Client()
        User.objects.create_user(
            username='kimson',
            email='kimson@naver.com',
            password='123456789kk'
        )
        print('Initialize create user account.')
    
    def setUp(self):
        profile = User.objects.get(id=1)
        print(f'{profile.username} generated!')
        
    def test_username(self):
        profile = User.objects.get(id=1)
        self.assertEqual(profile.username, 'kimson')
        
    def test_index_page(self):
        response = self.c.get(reverse('account:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/index.html')
        
    def test_login_page(self):
        response = self.c.get(reverse('account:signin'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/signin.html')
        
    def test_client_login(self):
        data = {
            'email': 'kimson@naver.com',
            'password': '123456789kk',
        }
        # 'username': 'kimson',
        # 'bio': '나는 도비다',
        res = self.c.post('/signin/', data)
        # print(res.content.decode('utf-8'))
        user = User.objects.get(id=1)
        self.assertTrue(user.is_authenticated)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'account/signin.html')
        # self.assertRedirects(response=res, expected_url='/?success=1', status_code=200)
        
    def test_signup_page(self):
        res = self.c.get(reverse('account:signup'))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'account/signup.html')
        
    def test_client_signup_fail(self):
        data = {
            'username':'dobby',
            'first_name':'james',
            'last_name':'dobby',
            'email':'dobby@naver.com',
            'password':'123456789',
            'bio':'나는 도비 아니다.',
        }
        res = self.c.post(reverse('account:signup'), data)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'account/signup.html')
        
    def tearDown(self):
        User.objects.all().delete()
        print('end')