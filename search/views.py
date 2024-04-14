from queue import Full
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q


from authentication.models import CloserUser
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


def search(request, name: str, current_city: str | None = None) -> HttpResponse:
    first_name, last_name = name.split(sep=" ")
    print(f"first name: {first_name} and last name: {last_name}")
    CloserUser.objects.filter(first_name=first_name, last_name=last_name)
    return HttpResponse("hello")
