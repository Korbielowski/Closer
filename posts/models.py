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
