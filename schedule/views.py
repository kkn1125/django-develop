from django.shortcuts import render, redirect

# Create your views here.
def schedule_list(request):
    return render(request, 'schedule/list.html')