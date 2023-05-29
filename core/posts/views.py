from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
import requests
import json
from core.posts.models import Posts, UserLikes
from django.db.models import F

def read_posts(id):
    posts = Posts.objects.all()
    context = []
    likes = UserLikes.objects.all()
    user_like = ""
    for i in likes:
        if i.user_id == id:
            user_like = i.likes
            break
    likes = user_like.split(",")
    for i in range(likes.count("")):
        likes.remove("")

    likes = [int(i) for i in likes]

    for post in posts:
        context.append({"id": post.id, "name": post.name, "body":post.comment, "likes": post.likes, "user_likes": likes, "comments": post.comments})
    return context

def make_post(request):
    if request.method == 'POST':
        comment = request.POST.get('comment') 
        if len(comment) >= 3:
            post = Posts(name=request.user.username, comment=comment, likes=0)
            post.save()
            return redirect('posts')
        else:
            messages.error(request, 'Publicação Precisa Ter Pelo Menos 3 caracteres! Por Favor, refaça a publicação!')
            return redirect('posts')
    return redirect('posts')


def like_post(request, post_id):
    likes = UserLikes.objects.all()
    user_like = ""
    id_in_bd = False
    for i in likes:
        if i.user_id == request.user.id:
            id_in_bd = True
            user_like = i.likes
            break
    l = user_like.split(",")
    l.pop()

    if str(post_id) in l:
        post_like = Posts.objects.get(id=post_id)
        post_like.likes = F('likes') - 1
        post_like.save()
        l.remove(str(post_id))
        for i in range(l.count('')):
            l.remove("")
        user_like = ",".join(l)
        user_like += ","
        user = UserLikes.objects.get(user_id=request.user.id)
        user.likes = user_like
        user.save()

    else:
        if id_in_bd:
            user_like += str(post_id) + ","
            print(user_like)
            user = UserLikes.objects.get(user_id=request.user.id)
            user.likes = user_like
            user.save()
        else:
            user_like += str(post_id) + ","
            user = UserLikes(user_id=request.user.id, likes=user_like)
            user.save()

        post_like = Posts.objects.get(id=post_id)
        post_like.likes = F('likes') + 1
        post_like.save()

    return HttpResponse(status=204)

@login_required(login_url='login')
def posts(request):
    context = {'data': read_posts(request.user.id)}
    if request.user.is_authenticated:
	    return render(request, 'dash/posts/index.html', context=context)
    return render(request, 'http_codes/page-404.html')
