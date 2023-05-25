from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def menu(request):
    if request.user.is_authenticated:
	    return render(request, 'dash/home/index.html')
    return render(request, 'http_codes/page-404.html')
