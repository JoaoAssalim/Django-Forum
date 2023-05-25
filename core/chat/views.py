from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def chat(request):
    if request.user.is_authenticated:
	    return render(request, 'dash/chat/index.html')
    return render(request, 'http_codes/page-404.html')
