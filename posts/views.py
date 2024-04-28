from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q

from .forms import PostForm


def create_post(request) -> HttpResponse:
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("profile", request.user.user_id)
    content = {"post_form": PostForm()}
    return render(request, "posts/post_creation.html", content)
