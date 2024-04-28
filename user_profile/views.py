from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q

from authentication.models import CloserUser, Friendship
from posts.models import Post
from utils.process_string import process_string


def profile(request, userID) -> HttpResponse:
    friends_to_accept = None
    if userID == request.user.user_id:
        friends_to_accept = Friendship.objects.filter(
            Q(accepting_user=request.user) | Q(status="pending")
        )
        if friends_to_accept:
            print(
                "Friend to accept",
                friends_to_accept[0].inviting_user.username,
                friends_to_accept[0].inviting_user.user_id,
                friends_to_accept[0].status,
            )

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
        Q(inviting_user=userID) | Q(accepting_user=userID) | Q(status="accepted")
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

    return render(
        request,
        "user_profile/user_profile.html",
        {
            "user_info": user_info[0],
            "user_name": user_name,
            "user_current_location": user_current_location,
            "user_home_location": user_home_location,
            "friends": friends,
            "friends_to_accept": friends_to_accept,
            "posts": posts,
        },
    )


# TODO: In the future add an option to edit the profile information
# def edit_profile_field(request, field) -> HttpResponse:
#     return HttpResponse("Editing profile")
