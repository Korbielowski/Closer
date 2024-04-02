from django.contrib import admin

from .models import CloserUser, Friendship

admin.site.register((CloserUser, Friendship))
