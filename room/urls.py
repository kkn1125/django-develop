from django.urls import path
from . import views

app_name = 'room'

urlpatterns = [
    path('room/', views.room_list, name='room_list')
]
