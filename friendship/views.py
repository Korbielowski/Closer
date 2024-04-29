from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q


from authentication.models import CloserUser, Friendship


def invitations_page(request) -> HttpResponse:
    friends_to_accept = None
    friends_to_accept = Friendship.objects.filter(
        Q(accepting_user=request.user) & Q(status="pending")
    )
    if friends_to_accept:
        print(
            "Friend to accept",
            friends_to_accept[0].inviting_user.username,
            friends_to_accept[0].inviting_user.user_id,
            friends_to_accept[0].status,
        )
    content = {
        "friends_to_accept": friends_to_accept,
    }
    return render(request, "friendship/invitations.html", content)


def send_invitation(request, userID) -> HttpResponse:
    if Friendship.objects.filter(
        Q(inviting_user=CloserUser(user_id=request.user.user_id))
        & Q(accepting_user=CloserUser(user_id=userID))
    ).count():
        print("Cannot send invitation second time")
        return redirect("search_page")
    friendship = Friendship(
        inviting_user=CloserUser(user_id=request.user.user_id),
        accepting_user=CloserUser(user_id=userID),
        status="pending",
    )
    friendship.save()
    print(
        "Sending invitation",
        friendship.accepting_user.username,
        friendship.inviting_user.user_id,
        friendship.status,
    )
    # print(Friendship.objects.all()[0].inviting_user)
    return redirect("search_page")


def accept_invitation(request, userID, state) -> HttpResponse:
    print("user to accept, from page", userID)
    print("accepting user", request.user.user_id)
    friend = Friendship.objects.get(
        inviting_user=userID, accepting_user=request.user.user_id, status="pending"
    )
    if state:
        friend.status = "accepted"
    else:
        friend.status = "declined"
    friend.save()
    print("state: ", state)
    print(
        "Accepting or declining",
        friend.accepting_user.username,
        friend.inviting_user.username,
        friend.status,
    )
    return redirect("invitations_page")
