from django.urls import path


from . import views


urlpatterns = [
    path("<str:name>/<str:current_city>/", views.search, name="search"),
]
