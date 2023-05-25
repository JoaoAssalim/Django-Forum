from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def singup(request):
	return render(request, 'dash/singup/index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        if User.objects.filter(email=email).exists():
            nome = User.objects.get(email=email).username
            user = auth.authenticate(username=nome, password=senha)
            print(user, nome, senha)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('menu')
            else:
                messages.info(request, 'Email or Password Invalid!')
                return redirect('login')
        else:
            messages.info(request, 'User not exists!')
            return redirect('login')
    return render(request, 'dash/login/index.html')
