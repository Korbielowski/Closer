from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q


from authentication.models import CloserUser, Friendship
from utils.process_string import process_string
from . import forms


# TODO: Replace search_page with just search (query: str, current_city: str | None = None)
def search_page(request) -> HttpResponse:
    content = {"search_form": forms.FullSearchForm()}
    if request.method != "POST":
        return render(request, "search/search_page.html", content)

    form = forms.FullSearchForm(request.POST)
    if not form.is_valid():
        messages.success(request, "Search was not valid :(")

    query: str = form.cleaned_data["query"]
    split_query = query.rsplit(" ")
    query_user = CloserUser.objects.filter(
        Q(first_name__in=split_query)
        | Q(second_name__in=split_query)
        | Q(last_name__in=split_query)
    )
    content["query_user"] = query_user
    return render(request, "search/search_page.html", content)


# TODO: Try to load a user info with this function, because it enables to call process_string function
# def load_user(request, user: CloserUser) -> HttpResponse:
#     pass


def add_friend(request, userID) -> HttpResponse:
    # if Friendship(
    #     Q(inviting_user=CloserUser(user_id=request.user.user_id))
    #     | Q(accepting_user=CloserUser(user_id=userID))
    #     | Q(status__in=("pending", "accepted", "declined"))
    # ):
    #     print("Cannot send invitation second time")
    #     return redirect("search_page")
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


def accept_friend(request, userID, state) -> HttpResponse:
    friend = Friendship.objects.get(
        Q(inviting_user=CloserUser(user_id=userID))
        | Q(accepting_user=CloserUser(user_id=request.user.user_id))
        | Q(status="pending")
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
    return redirect("profile", userID=request.user.user_id)


# def search(request, name: str, current_city: str | None = None) -> HttpResponse:
#     first_name, last_name = name.split(sep=" ")
#     print(f"first name: {first_name} and last name: {last_name}")
#     CloserUser.objects.filter(first_name=first_name, last_name=last_name)
#     return HttpResponse("hello")
