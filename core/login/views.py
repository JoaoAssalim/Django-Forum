from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def singup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        senha = request.POST.get('senha')
        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email already exists!')
            return redirect('singup')
        else:
            user = User.objects.create_user(name, email, senha)
            user.save()
            return redirect('login')
    return render(request, 'dash/singup/index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        if User.objects.filter(email=email).exists():
            nome = User.objects.get(email=email).username
            user = auth.authenticate(username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('feed')
            else:
                messages.info(request, 'Email or Password Invalid!')
                return redirect('login')
        else:
            messages.info(request, 'User not exists!')
            return redirect('login')
    return render(request, 'dash/login/index.html')
