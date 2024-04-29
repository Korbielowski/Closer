from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q

from authentication.models import CloserUser, Friendship
from posts.models import Post, Poll, Test
from utils.process_string import process_string


def profile(request, userID) -> HttpResponse:
    user_info = CloserUser.objects.filter(user_id=userID)
    user_name = process_string(
        user_info[0].first_name,
        [user_info[0].second_name, user_info[0].last_name],
        sep=" ",
    )
    user_current_location = process_string(
        user_info[0].current_city,
        [user_info[0].current_state, user_info[0].current_country],
        sep=", ",
    )
    user_home_location = process_string(
        user_info[0].home_city,
        [user_info[0].home_state, user_info[0].home_country],
        sep=", ",
    )
    friends_query = Friendship.objects.filter(
        Q(Q(inviting_user=userID) | Q(accepting_user=userID)) & Q(status="accepted")
    )
    friends = (
        (
            friend.accepting_user
            if friend.inviting_user.user_id == userID
            else friend.inviting_user
        )
        for friend in friends_query
    )

    posts = Post.objects.filter(user=userID)
    polls = Poll.objects.filter(author=userID)
    tests = Test.objects.filter(author=userID)

    return render(
        request,
        "user_profile/user_profile.html",
        {
            "user_info": user_info[0],
            "user_name": user_name,
            "user_current_location": user_current_location,
            "user_home_location": user_home_location,
            "friends": friends,
            "posts": posts,
            "polls": polls,
            "tests": tests,
        },
    )


# TODO: In the future add an option to edit the profile information
# def edit_profile_field(request, field) -> HttpResponse:
#     return HttpResponse("Editing profile")
