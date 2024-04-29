from django.urls import path


from . import views

urlpatterns = [
    path("", views.create_post, name="posts"),
    path("poll/", views.create_poll, name="polls"),
    path(
        "poll_answer/<int:poll_id>/<str:answer>", views.poll_answer, name="poll_answer"
    ),
    path("test/", views.create_test, name="tests"),
    path(
        "test_answer/<int:test_id>/<str:answer>", views.test_answer, name="test_answer"
    ),
]
