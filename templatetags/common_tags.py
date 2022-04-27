import random
from urllib import parse
from django import template
from django.core import serializers
from urllib.parse import quote_plus
from account.models import Profile

from room.models import UserInRoom

register = template.Library()

@register.simple_tag(name="set")
def set (value):
    return str(value)

@register.simple_tag(name="define")
def define (value):
    return value

@register.filter(name="set_title")
def set_title (value, arg=None):
    TEMP_TITLES = {
        "FRONT": ["안락한", "편안한", "슬기로운", "중요한", "새로운", "함께 나누는", "자유로운"],
        "MAIN": ["비즈니스", "일정 회의", "단체 회의", "주간 회의", "협력사 회의"],
    }
    title_front = TEMP_TITLES['FRONT']
    title_main = TEMP_TITLES['MAIN']
    front_idx = random.randrange(0, len(title_front))
    main_idx = random.randrange(0, len(title_main))
    value.initial.setdefault('title', f'{TEMP_TITLES["FRONT"][front_idx]} {TEMP_TITLES["MAIN"][main_idx]}')
    return value

@register.filter(name="has_key")
def has_key (value, arg=None):
    query = value.get('q')
    query_set = parse.parse_qs(query)
    
    if arg in query_set:
        return True
    
    return False

@register.filter(name="select_msg")
def select_msg (value):
    query = value.get('q')
    query_set = parse.parse_qs(query)
    username = query_set['name'][0] if 'name' in query_set else None
    if 'success' in query_set:
        match query_set['success'][0]:
            case '1': return f'✅ {username}님의 계정이 성공적으로 로그아웃 되었습니다.'
            case '2': return f'✅ {username}님 회원가입에 성공했습니다.'
    elif 'error' in query_set:
        match query_set['error'][0]:
            case '1': return ''

@register.filter(name="user_list")
def user_list (value):
    users_list = UserInRoom.objects.filter(room_id=value)
    mapped_list = map(lambda x: x['user_id'],list(users_list.values()))
    users_lists = Profile.objects.filter(pk__in=mapped_list)
    
    return list(users_lists)

@register.filter(name="strip")
def strip (value):
    return str.strip(value)

@register.filter(name="toJson")
def toJson (value):
    print(value)
    if type(value) == list:
        jsonify = serializers.serialize("json", value)
    else:
        jsonify = serializers.serialize("json", [value])
    # 배열형태에 있어야 시리얼라이즈 가능함
    parsed_code = quote_plus(jsonify)
    return parsed_code

@register.filter(name="default_field")
def default_field(value, arg):
    value.initial = arg
    print(arg)
    return value

@register.filter(name="default_form")
def default_form(value, arg):
    [k, v] = arg.split('/')
    value.initial.setdefault(k, v)
    return value

@register.filter(name="users_in_room")
def users_in_room(value, arg=0):
    user_list = UserInRoom.objects.filter(room_id=value).exclude(user_id=arg)
    # exclude 조건 부정문, arg는 master의 pk를 받는다. 혹은 필터 후 제외할 유저 pk를 받는다
    return user_list