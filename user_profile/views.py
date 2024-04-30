from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q

import math

from authentication.models import CloserUser, Friendship
from posts.models import Post, Poll, Test, UserPollAnswer, UserTestAnswer
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
    polls_query = Poll.objects.filter(author=userID)
    tests_query = Test.objects.filter(author=userID)

    polls = []
    tests = []

    for poll_query in polls_query:
        tmp = []
        if poll_query.votes != 0:
            first = math.ceil(
                UserPollAnswer.objects.filter(
                    Q(poll=poll_query) & Q(answer=poll_query.first_ans)
                ).count()
                / poll_query.votes
                * 100
            )
            second = math.ceil(
                UserPollAnswer.objects.filter(
                    Q(poll=poll_query) & Q(answer=poll_query.second_ans)
                ).count()
                / poll_query.votes
                * 100
            )
            third = math.ceil(
                UserPollAnswer.objects.filter(
                    Q(poll=poll_query) & Q(answer=poll_query.third_ans)
                ).count()
                / poll_query.votes
                * 100
            )
            fourth = math.ceil(
                UserPollAnswer.objects.filter(
                    Q(poll=poll_query) & Q(answer=poll_query.fourth_ans)
                ).count()
                / poll_query.votes
                * 100
            )
        else:
            first, second, third, fourth = 0, 0, 0, 0
        tmp.append(poll_query)
        tmp.append((first, second, third, fourth))
        polls.append(tmp)

        for test_query in tests_query:
            tmp = []
            if poll_query.votes != 0:
                first = math.ceil(
                    UserTestAnswer.objects.filter(
                        Q(test=test_query) & Q(answer=test_query.first_ans)
                    ).count()
                    / test_query.votes
                    * 100
                )
                second = math.ceil(
                    UserTestAnswer.objects.filter(
                        Q(test=test_query) & Q(answer=test_query.second_ans)
                    ).count()
                    / test_query.votes
                    * 100
                )
                third = math.ceil(
                    UserTestAnswer.objects.filter(
                        Q(test=test_query) & Q(answer=test_query.third_ans)
                    ).count()
                    / test_query.votes
                    * 100
                )
                fourth = math.ceil(
                    UserTestAnswer.objects.filter(
                        Q(test=test_query) & Q(answer=test_query.fourth_ans)
                    ).count()
                    / test_query.votes
                    * 100
                )
            else:
                first, second, third, fourth = 0, 0, 0, 0
            # correct =
            tmp.append(test_query)
            tmp.append((first, second, third, fourth))
            tests.append(tmp)

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
