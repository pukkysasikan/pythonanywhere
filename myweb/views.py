from django.shortcuts import render , redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required


def index(request):
    articles = Article.objects.all()
    return render(request,'myweb/index.html', {'articles':articles})


def food(request):
    food = Food.objects.all()
    return render(request,'myweb/foods.html', {'food':food})

@login_required
def article(request, id):
    article = Article.objects.get(pk=id)
    return render(request,'myweb/Article.html', {'article':article})


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


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'myweb/signup.html', {'form': form})