from django.test import Client, TestCase
from django.urls import reverse
from account.models import Profile
from django.contrib.auth import get_user_model

from room.models import Room


"""_중요_
로그인 처리할 때 modelForm에서 email로 로그인 처리하게 설정 했으면
테스트 코드 작성시에도 email로 로그인 시도해야 정상작동한다.
"""

# Create your tests here.
class TestRoom(TestCase):
    def setUp(self):
        """_summary_
        """
        self.c = Client()
        Profile.objects.create_user(
            id=1,
            username='test',
            email='test@naver.com',
            password='1234'
        )
    
    # def test_room_create(self):
    #     """_룸 생성 폼으로 들어가는 테스트_
    #     """
    #     self.c.force_login(Profile.objects.get(pk=1))
    #     res = self.c.get(reverse('room:create'))
    #     self.assertTrue(res.status_code == 200)
        
    def test_remove_room(self):
        Room.objects.create(
            master_id = 1,
            title='test',
            desc='test'
        )
        self.assertEqual(len(Room.objects.all()), 1)
        res = self.c.post(reverse('room:out', kwargs={'id': 1}))
        self.assertEqual(res.status_code, 302)
        all = Room.objects.all()
        print(all)
        self.assertEqual(len(all), 0)
        
    def tearDown(self):
        """_summary_
        """
        self.c.logout()