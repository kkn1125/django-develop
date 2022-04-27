from django.db import models
from django.utils import timezone
from account.models import Profile

# Create your models here.
class Room(models.Model):
    id = models.AutoField(primary_key=True)
    master = models.ForeignKey(Profile, on_delete=models.CASCADE , related_name='master_id')
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='방 제목')
    desc = models.CharField(max_length=300, null=True, blank=True, verbose_name='방 설명')
    regdate = models.DateTimeField(auto_now_add=True)
    updates = models.DateTimeField(auto_now=True)

class UserInRoom(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    regdate = models.DateTimeField(auto_now_add=True)

class Invite(models.Model):
    id = models.AutoField(primary_key=True)
    caller = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='caller')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    regdate = models.DateTimeField(auto_now_add=True)