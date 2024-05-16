from django.db import models
from django.db.models import Q
import math

from authentication.models import CloserUser


class UserContent(models.Model):
    TYPE = (("post", "post"), ("poll", "poll"), ("test", "test"))
    user = models.ForeignKey(CloserUser, default=None, on_delete=models.CASCADE)
    creation_date = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=4, choices=TYPE)


class Post(models.Model):
    user = models.ForeignKey(
        CloserUser, default=None, on_delete=models.CASCADE, related_name="user"
    )
    creation_date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to="posts_images/", blank=True)

    def get_name(self) -> str:
        return self.__class__.__name__


class Poll(models.Model):
    author = models.ForeignKey(CloserUser, default=None, on_delete=models.CASCADE)
    creation_date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100, default="")
    question = models.CharField(max_length=500)
    first_ans = models.CharField(max_length=500)
    second_ans = models.CharField(max_length=500)
    third_ans = models.CharField(max_length=500)
    fourth_ans = models.CharField(max_length=500)
    votes = models.IntegerField(default=0)

    def get_name(self) -> str:
        return self.__class__.__name__

    def get_ans(self) -> tuple[str, str, str, str]:
        output = (
            str(
                math.ceil(
                    UserPollAnswer.objects.filter(
                        Q(poll=self) & Q(answer=self.first_ans)
                    ).count()
                    / self.votes
                    * 100
                )
            ),
            str(
                math.ceil(
                    UserPollAnswer.objects.filter(
                        Q(poll=self) & Q(answer=self.second_ans)
                    ).count()
                    / self.votes
                    * 100
                )
            ),
            str(
                math.ceil(
                    UserPollAnswer.objects.filter(
                        Q(poll=self) & Q(answer=self.third_ans)
                    ).count()
                    / self.votes
                    * 100
                )
            ),
            str(
                math.ceil(
                    UserPollAnswer.objects.filter(
                        Q(poll=self) & Q(answer=self.fourth_ans)
                    ).count()
                    / self.votes
                    * 100
                )
            ),
        )
        return output


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

    def get_name(self) -> str:
        return self.__class__.__name__

    def get_ans(self) -> tuple[str, str, str, str]:
        output = (
            str(
                math.ceil(
                    UserTestAnswer.objects.filter(
                        Q(test=self) & Q(answer=self.first_ans)
                    ).count()
                    / self.votes
                    * 100
                )
            ),
            str(
                math.ceil(
                    UserTestAnswer.objects.filter(
                        Q(test=self) & Q(answer=self.second_ans)
                    ).count()
                    / self.votes
                    * 100
                )
            ),
            str(
                math.ceil(
                    UserTestAnswer.objects.filter(
                        Q(test=self) & Q(answer=self.third_ans)
                    ).count()
                    / self.votes
                    * 100
                )
            ),
            str(
                math.ceil(
                    UserTestAnswer.objects.filter(
                        Q(test=self) & Q(answer=self.fourth_ans)
                    ).count()
                    / self.votes
                    * 100
                )
            ),
        )
        return output


class UserTestAnswer(models.Model):
    test = user = models.ForeignKey(Test, default=None, on_delete=models.CASCADE)
    user = models.ForeignKey(CloserUser, default=None, on_delete=models.CASCADE)
    answer = models.CharField(max_length=500)
    answer_date = models.DateField(auto_now_add=True)
