from django.db import models


from authentication.models import CloserUser


class Post(models.Model):
    user = models.ForeignKey(
        CloserUser, default=None, on_delete=models.CASCADE, related_name="user"
    )
    creation_date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to="posts_images/", blank=True)


class Poll(models.Model):
    author = models.ForeignKey(
        CloserUser, default=None, on_delete=models.CASCADE, related_name="author"
    )
    creation_date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100, default="")
    question = models.CharField(max_length=500)
    first_ans = models.CharField(max_length=500)
    second_ans = models.CharField(max_length=500)
    third_ans = models.CharField(max_length=500)
    fourth_ans = models.CharField(max_length=500)
    votes = models.IntegerField(default=0)


class UserPollAnswer(models.Model):
    poll = user = models.ForeignKey(
        Poll, default=None, on_delete=models.CASCADE, related_name="poll"
    )
    user = models.ForeignKey(
        CloserUser, default=None, on_delete=models.CASCADE, related_name="respondent"
    )
    answer = models.CharField(max_length=500)
    answer_date = models.DateField(auto_now_add=True)


class Test(models.Model):
    author = models.ForeignKey(CloserUser, default=None, on_delete=models.CASCADE)
    creation_date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100, default="")
    question = models.CharField(max_length=500)
    first_ans = models.CharField(max_length=500)
    second_ans = models.CharField(max_length=500)
    third_ans = models.CharField(max_length=500)
    fourth_ans = models.CharField(max_length=500)
    correct_ans = models.CharField(max_length=500)
    votes = models.IntegerField(default=0)


class UserTestAnswer(models.Model):
    poll = user = models.ForeignKey(Poll, default=None, on_delete=models.CASCADE)
    user = models.ForeignKey(CloserUser, default=None, on_delete=models.CASCADE)
    answer = models.CharField(max_length=500)
    answer_date = models.DateField(auto_now_add=True)
