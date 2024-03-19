from django.contrib.auth.models import AbstractUser
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

# from .managers import CloserUserManager


# TODO: In the future test whether AbstractBaseUser would not suite the application needs better
class CloserUser(AbstractUser):
    RELIGIONS = (
        ("Unspecified", "Unspecified"),
        ("Christianity", "Christianity"),
        ("Islam", "Islam"),
        ("Hinduism", "Hinduism"),
        ("Buddhism", "Buddhism"),
        ("Shinto", "Shinto"),
        ("Taoism", "Taoism"),
        ("Voodoo", "Voodoo"),
        ("Folk religion", "Folk religion"),
        ("Atheism", "Atheism"),
    )
    RELATIONSHIPS = (
        ("Unspecified", "Unspecified"),
        ("Single", "Single"),
        ("Married", "Married"),
        ("Engaged", "Engaged"),
        ("Complicated", "Complicated"),
        ("Divorced", "Divorced"),
        ("Widowed", "Widowed"),
        ("Polyamorous", "Polyamorous"),
        ("FWB", "FWB"),
    )
    GENDERS = (
        ("Unspecified", "Unspecified"),
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
        ("Helikopter szturmowy", "Helikopter szturmowy"),
    )
    user_id = models.AutoField(primary_key=True)
    creation_date = models.DateField(auto_now_add=True)
    first_name = models.CharField(max_length=70)
    second_name = models.CharField(max_length=70, blank=True)
    last_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70, unique=True)
    username = models.CharField(blank=True, null=True, max_length=100)
    phone_number = models.CharField(max_length=15, blank=True)
    date_of_birth = models.DateField(null=True)
    current_city = models.CharField(max_length=85, blank=True)
    current_state = models.CharField(max_length=85, blank=True)
    current_country = models.CharField(max_length=28, blank=True)
    home_city = models.CharField(max_length=85, blank=True)
    home_state = models.CharField(max_length=85, blank=True)
    home_country = models.CharField(max_length=28, blank=True)
    profile_picture_url = models.ImageField(upload_to="profile_picture/", blank=True)
    background_picture_url = models.ImageField(
        upload_to="background_picture/", blank=True
    )
    about_me = models.CharField(max_length=150, blank=True)
    education = models.CharField(max_length=100, blank=True)
    religion = models.CharField(max_length=20, choices=RELIGIONS, blank=True)
    relationship = models.CharField(max_length=20, choices=RELATIONSHIPS, blank=True)
    gender = models.CharField(max_length=20, choices=GENDERS, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "username"]
