from django.urls import path


from . import views


urlpatterns = [
    # path("<str:name>/<str:current_city>/", views.search, name="search"),
    path("", views.search_page, name="search_page"),
    # path("<str:name>", views.search, name="search"),
    path("add_friend/<int:userID>", views.add_friend, name="add_friend"),
    path(
        "accept_friend/<int:userID>/<int:state>",
        views.accept_friend,
        name="accept_friend",
    ),
]
