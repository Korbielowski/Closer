from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q

from itertools import chain
import operator

from authentication.models import Friendship

from posts.models import Post, Poll, Test, Short


def feed(request) -> HttpResponse:
    friends_query = Friendship.objects.filter(
        Q(Q(inviting_user=request.user) | Q(accepting_user=request.user))
        & Q(status="accepted")
    )
    friends = [
        (
            friend.accepting_user
            if friend.inviting_user.user_id == request.user.user_id
            else friend.inviting_user
        )
        for friend in friends_query
    ]

    tests = Test.objects.filter(author__in=friends)
    posts = Post.objects.filter(user__in=friends)
    polls = Poll.objects.filter(author__in=friends)

    # TODO: Maybe use union like this: query.union(query_poll, query_test, all=True)
    sorted_query = sorted(
        tuple(chain(posts, polls, tests)), key=operator.attrgetter("creation_date")
    )

    media = []

    for med in sorted_query:
        if med.get_name() == "Post":
            media.append((med,))
        elif med.get_name() == "Poll":
            media.append((med, med.get_ans()))
        elif med.get_name() == "Test":
            media.append((med, med.get_ans()))

    content = {"media": media}

    return render(request, "feed/feed.html", content)


def feed_shorts(request) -> HttpResponse:
    friends_query = Friendship.objects.filter(
        Q(Q(inviting_user=request.user) | Q(accepting_user=request.user))
        & Q(status="accepted")
    )
    friends = [
        (
            friend.accepting_user
            if friend.inviting_user.user_id == request.user.user_id
            else friend.inviting_user
        )
        for friend in friends_query
    ]

    shorts = Short.objects.filter(user__in=friends)
    for short in shorts:
        print(short.title, short.video, short.video.url)
    content = {"shorts": shorts}

    return render(request, "feed/shorts.html", content)
