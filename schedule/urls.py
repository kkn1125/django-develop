from django.urls import path
from . import views

app_name = 'schedule'

urlpatterns = [
    path('schedule/', views.schedule_list, name='schedule')
]
