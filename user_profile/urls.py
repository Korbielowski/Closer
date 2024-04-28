from django.urls import path


from . import views
from authentication.views import logout

urlpatterns = [
    path("<int:userID>", views.profile, name="profile"),
    path("edit_profile_field/", views.edit_profile_field, name="edit_profile_filed"),
]
