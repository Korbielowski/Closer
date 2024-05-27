from django.db import models
from django.utils.html import format_html

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

    def get_rank_icon(self):
        if self.rank == self.Rank.NEWUSER:
            return format_html("<span class='material-symbols-outlined ranks' title='New User'>kid_star</span>")
        elif self.rank == self.Rank.INTERMEDIATE:
            return format_html("<span class='material-symbols-outlined ranks' title='Intermediate'>star</span>")
        elif self.rank == self.Rank.PRO:
            return format_html("<span class='material-symbols-outlined ranks' title='Pro'>star_half</span>")
        elif self.rank == self.Rank.HACKER:
            return format_html("<span class='material-symbols-outlined ranks' title='Hacker'>hotel_class</span>")


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
    
    def get_badge_icon(self):
        output = ""
        if self.new_user_badge == self.Badges.NEWUSER:
            output += "<span class='material-symbols-outlined' title='Newbie'>accessibility_new</span>"

        if self.poster_badge == self.Badges.POSTER:
            output += "<span class='material-symbols-outlined' title='Poster'>post</span>"

        if self.shorter_badge == self.Badges.SHORTER:
            output += "<span class='material-symbols-outlined' title='Shorter'>straighten</span>"

        if self.poller_badge == self.Badges.POLLER:
            output += "<span class='material-symbols-outlined' title='Poller'>ballot</span>"

        if self.tester_badge == self.Badges.TESTER:
            output += "<span class='material-symbols-outlined' title='Tester'>quiz</span>"

        return format_html(output)
