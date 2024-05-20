from django.urls import path

from . import views

urlpatterns = [path("", views.feed, name="feed"),
               path("shorts/", views.feed, name="feed_shorts"),
               ]
