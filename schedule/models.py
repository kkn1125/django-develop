from django.db import models
from account.models import Profile
from django.utils import timezone

from room.models import Room

# Create your models here.
class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, null=False, blank=False)
    content = models.CharField(max_length=500, null=True, blank=True)
    coworker = models.CharField(max_length=300, null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    regdate = models.DateTimeField(auto_now_add=True)
    updates = models.DateTimeField(auto_now=True)