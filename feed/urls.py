from django.urls import path

from . import views

urlpatterns = [path("", views.feed, name="feed"),
               path("shorts/", views.feed_shorts, name="feed_shorts"),
               ]
