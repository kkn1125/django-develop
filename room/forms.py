from account.models import Profile
from .models import Room, UserInRoom, Invite
from django.forms import CharField, ModelChoiceField, ModelForm, NumberInput, TextInput

class RoomForm(ModelForm):
    """_ModelChoiceField_
    queryset 설정으로 modelform에서 request.POST 내용을 자동으로 할당받기 위함
    """
    master = ModelChoiceField(queryset=Profile.objects.all(), label='', widget=NumberInput(attrs={'ghost': True}))
    class Meta:
        model = Room
        fields = [
            'master',
            'title',
            'desc',
        ]
        widgets = {
            'title': TextInput(attrs={'placeholder':'제목을 입력하세요.'}),
            'desc': TextInput(attrs={'placeholder':'방에 대한 설명을 간략하게 적어주세요.'}),
        }
        
class UserInRoomForm(ModelForm):
    class Meta:
        model = UserInRoom
        fields = [
            'user',
            'room',
        ]
        
class InviteForm(ModelForm):
    class Meta:
        model = Invite
        fields = [
            'caller',
            'receiver',
            'room',
        ]