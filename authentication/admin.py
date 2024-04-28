from django.contrib import admin

from .models import CloserUser, Friendship
from posts.models import Post

admin.site.register((CloserUser, Friendship, Post))
