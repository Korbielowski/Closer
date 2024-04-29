from django.contrib import admin

from .models import CloserUser, Friendship
from posts.models import Post, Poll, UserPollAnswer, Test, UserTestAnswer

admin.site.register(
    (CloserUser, Friendship, Post, Poll, UserPollAnswer, Test, UserTestAnswer)
)
