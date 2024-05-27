from email.policy import default
from django.db import models

from authentication.models import CloserUser


class UserRanks(models.Model):
    class Rank(models.TextChoices):
        NEWUSER = "NewUser"
        INTERMEDIATE = "Intermediate"
        PRO = "Pro"
        HACKER = "Hacker"
    user = models.ForeignKey(CloserUser, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    rank = models.CharField(max_length=20, choices=Rank, default=Rank.NEWUSER)

    def new_rank(self):
        if self.points <= 5:
            return self.Rank.NEWUSER
        if 5 < self.points <= 10:
            return self.Rank.INTERMEDIATE
        elif 10 < self.points <= 20:
            return self.Rank.PRO
        elif 20 < self.points:
            return self.Rank.HACKER

class Badges(models.Model):
    class Badges(models.TextChoices):
        NEWUSER = "1"
        POSTER = "2"
        SHORTER = "3"
        POLLER = "4"
        TESTER = "5" 
    user = models.ForeignKey(CloserUser, on_delete=models.CASCADE)
    new_user_badge = models.CharField(max_length=20, choices=Badges, default=Badges.NEWUSER)
    poster_badge = models.CharField(max_length=20, choices=Badges, default="")
    shorter_badge = models.CharField(max_length=20, choices=Badges, default="")
    poller_badge = models.CharField(max_length=20, choices=Badges, default="")
    tester_badge = models.CharField(max_length=20, choices=Badges, default="")

