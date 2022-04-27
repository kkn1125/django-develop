from django.urls import path
from . import views

app_name = 'room'

urlpatterns = [
    path('form/', views.room_create, name='create'),
    path('edit/<int:id>', views.room_edit, name='edit'),
    path('enter/<int:id>', views.room_enter, name='enter'),
    path('out/<int:id>', views.room_out, name='out'),
    path('invite/<int:uid>', views.room_invite, name='invite'),
    path('answer/<int:uid>', views.room_answer, name='answer'),
]
