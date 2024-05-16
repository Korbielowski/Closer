from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q

from itertools import chain
import operator

from authentication.models import CloserUser, Friendship
from posts.models import Post, Poll, Test, UserPollAnswer
from user_profile.views import profile


def feed(request) -> HttpResponse:
    friends_query = Friendship.objects.filter(
        Q(Q(inviting_user=request.user) | Q(accepting_user=request.user)) & Q(status="accepted"))
    friends = [
            ( friend.accepting_user
            if friend.inviting_user.user_id == request.user.user_id
            else friend.inviting_user)
            for friend in friends_query 
    ]

    tests = Test.objects.filter(author__in=friends)
    posts = Post.objects.filter(user__in=friends)
    polls = Poll.objects.filter(author__in=friends)

    # TODO: Maybe use union like this: query.union(query_poll, query_test, all=True)
    media = sorted(tuple(chain(posts, polls, tests)), key=operator.attrgetter("creation_date"))
    content = {"content": media}

    print("User created content:\n", *media)

    return render(request, "feed/feed.html", content)
