from django.urls import path

from . import views

urlpatterns = [
    path("", views.invitations_page, name="invitations_page"),
    path("send_invitation/<int:userID>", views.send_invitation, name="send_invitation"),
    path(
        "accept_invitation/<int:userID>/<int:state>",
        views.accept_invitation,
        name="accept_invitation",
    ),
]
