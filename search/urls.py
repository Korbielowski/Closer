from django.urls import path


from . import views


urlpatterns = [
    path("", views.search_page, name="search_page"),
    # path("<str:name>/<str:current_city>/", views.search, name="search"),
    # path("<str:name>", views.search, name="search"),
]
