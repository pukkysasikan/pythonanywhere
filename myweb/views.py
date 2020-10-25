from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Question, Choice
from django.contrib import messages


def index(request):
    return render(request,'myweb/index.html')

def fruit(request):
    return render(request,'myweb/fruit.html')

def foodlowkcal(request):
    return render(request,'myweb/foodlowkcal.html')

def foodlowkcalat(request):
    return render(request,'myweb/foodlowkcalat.html')

def howtoeat(request):
    return render(request,'myweb/howtoeat.html')

def howtodrink(request):
    return render(request,'myweb/howtodrink.html')


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง')

        context = {}
        return render(request, '/', context)

def logout_user(request):
    logout(request)
    return redirect('/')

#def detail(request, question_id):
   # return render(request, 'myweb/detail.html')

#def results(request, question_id):
    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % question_id)

#def vote(request, question_id):
    #return HttpResponse("You're voting on question %s." % question_id)