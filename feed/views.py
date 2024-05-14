from django.shortcuts import render
from django.http import HttpResponse

from authentication.models import CloserUser
from posts.models import Post, Poll, Test, UserPollAnswer


def feed(request) -> HttpResponse:
    #Post.objects.filter()
    return render(request, "feed/feed.html")
