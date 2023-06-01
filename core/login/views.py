from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.views import View
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView, RedirectView

class SignupView(View):
    template_name = 'dash/signup/index.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        email = request.POST.get('email')
        name = request.POST.get('name')
        senha = request.POST.get('senha')
        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email already exists!')
            return redirect('signup')
        else:
            user = User.objects.create_user(name, email, senha)
            user.save()
            return redirect('login')


class LoginView(View):
    template_name = 'dash/login/index.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        if User.objects.filter(email=email).exists():
            nome = User.objects.get(email=email).username
            user = auth.authenticate(username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                return redirect('feed')
            else:
                messages.info(request, 'Email or Password Invalid!')
                return redirect('login')
        else:
            messages.info(request, 'User does not exist!')
            return redirect('login')

@login_required
def profile(request):
    return render(request, 'dash/profile/index.html')