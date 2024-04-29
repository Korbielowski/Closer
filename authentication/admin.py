from django.contrib import admin

from .models import CloserUser, Friendship
from posts.models import Post, Poll, UserPollAnswer

admin.site.register((CloserUser, Friendship, Post, Poll, UserPollAnswer))
