from urllib import parse
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from account.models import Profile
from .forms import RoomForm, UserInRoomForm
from .models import Invite, Room, UserInRoom
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required

# Create your views here.
@api_view(['GET', 'POST'])
@login_required
def room_create(request):
    if request.method == 'POST':
        master = request.POST['master']
        title = request.POST['title']
        desc = request.POST['desc']
        room = Room(
            master_id=master,
            title=title,
            desc=desc,
        )
        room.save()
        
        user_in_room = UserInRoom(
            user_id=master,
            room_id=room.pk,
        )
        
        user_in_room.save()
        
        return redirect(reverse('room:enter', kwargs={'id':room.pk}))
    else:
        form = RoomForm()
        
    context = {
        "form": form
    }
    
    return render(request, 'room/create.html', context)

@api_view(['GET', 'POST'])
def room_edit(request, id):
    
    if request.method == 'POST':
        find_room = Room.objects.filter(pk=id)

        if find_room.exists():
            room = find_room.get(pk=id)
            form = RoomForm(request.POST, instance=room)
            if form.is_valid():
                form_confirm = form.save(commit=False)
                form_confirm.save()
                
            return redirect(reverse('room:enter', kwargs={'id':room.pk}))
    else:
        find_room = Room.objects.filter(pk=id)
        if find_room.exists():
            room = find_room.get(pk=id)
            form = RoomForm(instance=room)

        # 초대 대기 중인 인원들
        invite_list = Invite.objects.filter(room_id=room.pk)

        # 방에 참여한 인원 목록
        user_list = UserInRoom.objects.filter(room_id=room.pk)
        
        # 방 참여 인원 id
        joined_user_list = list(map(lambda x: x.user_id, list(user_list)))
        
        # 초대 중인 인원 id
        invited_user_list = list(map(lambda x: x.receiver_id, list(invite_list)))
        
        # 참여인원 제외한 모든 유저 목록
        users = Profile.objects.exclude(pk__in=joined_user_list+invited_user_list)
        
    context = {
        "form": form,
        "room": room,
        "user_list": user_list,
        "users": users,
    }
    
    return render(request, 'room/edit.html', context)

@api_view(['GET'])
def room_enter(request, id):
    is_room = Room.objects.filter(id=id)
    if is_room.exists():
        room = is_room.get(id=id)
        context = {
            "room": room,
            "id": room.pk
        }
        return render(request, 'room/enter.html', context)
    return redirect(reverse('account:index')+'?q='+parse.quote('error=1'))

@api_view(['POST'])
def room_out(request, id):
    if request.method == 'POST':
        user_id = request.POST.get('id')
        room_id = id
        found_user_in_room = UserInRoom.objects.filter(room_id=room_id, user_id=user_id)
        found_user_in_room.delete()
        Room.objects.filter(id=room_id).delete()
    return redirect(reverse('account:index') + '?q=' + parse.quote('success=1'))

@api_view(['POST'])
def room_invite(request, uid):
    if request.method == 'POST':
        room_id = request.POST['rid']
        invite = Invite(
                caller_id=request.user.pk,
                receiver_id=uid,
                room_id=room_id
            )
        invite.save()
        
    return redirect(reverse('account:index') + '?q=' + parse.quote('success=1'))

@api_view(['POST'])
def room_answer(request, uid):
    if request.method == 'POST':
        room_id = request.POST['rid']
        answer = request.POST['answer']
        cid = request.POST['cid']
        if answer == '1':
            # 수락
            user_in_room = UserInRoom(
                user_id=uid,
                room_id=room_id
            )
            user_in_room.save()
        elif answer == '0':
            # 거절
            pass
        
        Invite.objects.filter(room_id=room_id, receiver_id=uid, caller_id=cid).delete()
        
    return redirect(reverse('account:index') + '?q=' + parse.quote('success=3'))