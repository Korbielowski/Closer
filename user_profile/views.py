import re  # Strange import
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.http import HttpResponse

from authentication.models import CloserUser
from utils.process_string import process_string


def profile(request, username) -> HttpResponse:
    user_info = CloserUser.objects.filter(email=request.user.email)
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
    return render(
        request,
        "user_profile/user_profile.html",
        {
            "user_info": user_info[0],
            "user_name": user_name,
            "user_current_location": user_current_location,
            "user_home_location": user_home_location,
        },
    )


def edit_profile_field(request, field) -> HttpResponse:
    return HttpResponse("Editing profile")
