from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    users = User.objects.all()
    return render(request,'index.html',{'users':users})

def add_data(request):
    if request.method == 'POST':
        User.objects.create(
            name = request.POST['name'],
            email = request.POST['email'],
            password = request.POST['pwd']
        )
        
        users = list(User.objects.values())
        return JsonResponse({'msg':"Data Created", 'users':users})
    

@csrf_exempt
def delete_data(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.POST['id'])
        user.delete()

        users = list(User.objects.values())
        return JsonResponse({'msg':"Data Deleted", 'users':users})
