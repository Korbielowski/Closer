from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.http import HttpResponse

from authentication.models import CloserUser


def search(request, name: str, current_city: str | None) -> HttpResponse:
    first_name, last_name = name.split(sep=" ")
    CloserUser.objects.filter(first_name=first_name, last_name=last_name)
    return HttpResponse("hello")
