from django.forms import ValidationError
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.http import HttpResponse

from . import forms, models

# TODO: Add proper messages when logging in, singing up and logging out. Messages pop ups (probably html modals)


def index(request) -> HttpResponse:
    content = {"login_form": forms.LoginForm()}
    return render(request, "authentication/index.html", content)


def login(request) -> HttpResponse:
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(
                username=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                auth.login(request, user)
                messages.success(request, "Logged in successfully :)")
                return redirect("profile")
            else:
                messages.success(
                    request, "Email or password is wrong. Please try again"
                )
                return redirect("index")
    return redirect("index")


def signup(request) -> HttpResponse:
    if request.method == "POST":
        form = forms.SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            try:
                validate_password(password=request.POST["password"], user=user)
            except ValidationError:
                # TODO: Better password validation message and dont remove user info from signup form
                messages.success(request, "Your password is too weak")
                return redirect("signup")
            else:
                user.password = make_password(request.POST["password"])
                user.save()
                user = auth.authenticate(
                    username=form.cleaned_data["email"],
                    password=form.cleaned_data["password"],
                )
                auth.login(request, user)
                messages.success(request, "Signed up successfully :)")
                return redirect("profile")
        messages.success(
            request, "It looks like You have an active account. Please try login in."
        )
        # TODO: Save path to profile picture and background picture in db. Hash mobile phone number and email (Python secrets or something from Django).
    content = {"signup_form": forms.SignupForm()}
    return render(request, "authentication/signup.html", content)


def logout(request) -> HttpResponse:
    auth.logout(request)
    messages.success(request, "Logged out successfully :)")
    return redirect("index")
