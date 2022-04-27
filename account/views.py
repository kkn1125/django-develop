from urllib import parse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.urls import reverse
from rest_framework.decorators import api_view
from room.models import UserInRoom, Invite, Room

from .forms import SigninForm, SignupForm

# Create your views here.
@api_view(['GET'])
def index(request):
    # 유저가 참여한 방 목록
    room_num_list = list(map(lambda x: x['room_id'], UserInRoom.objects.filter(user_id=request.user.id).values()))
    
    # 참여한 방의 DB정보 목록
    room_list = Room.objects.filter(pk__in=room_num_list).order_by("regdate");
    
    # 초대 목록
    invite_list = Invite.objects.filter(receiver_id=request.user.pk)
    
    context = {
        "rooms": room_list,
        "invites": invite_list
    }
    return render(request, 'account/index.html', context)

@api_view(['GET', 'POST'])
def signin(request):
    if request.method == 'POST':
        form = SigninForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                # user 검증해놓고 왜 form.get_user() 메서드를 사용했는지...;
                login(request, user)
                return redirect(reverse('account:index')+'?success=1')
    else:
        form = SigninForm()
    return render(request, 'account/signin.html', {'form':form})

@api_view(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            sign = form.save(commit=False)
            sign.save()
            return redirect(reverse('account:signin')+'?q='+parse.quote(f'success=2&name={sign.username}'))
    else:
        form = SignupForm()
    return render(request, 'account/signup.html', {'form':form})

@api_view(['GET', 'POST'])
def signout(request):
    username = request.user.username
    logout(request)
    return redirect(reverse('account:signin')+'?q='+parse.quote(f'success=1&name={username}'))
