from django.shortcuts import render

# Create your views here.
def room_list(request):
    return render(request, 'room/list.html')