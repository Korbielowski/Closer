from django import forms
from .models import CloserUser

from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumber

# TODO: Forms should be remade so that they use modelForms instead of normal Forms


class LoginForm(forms.Form):
    email = forms.CharField(
        max_length=70,
        required=True,
        widget=forms.EmailInput(
            attrs={"placeholder": "Email", "name": "email", "class": "email"}
        ),
    )
    password = forms.CharField(
        max_length=70,
        required=True,
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "name": "password", "class": "password"}
        ),
    )


class SignupForm(forms.ModelForm):

    class Meta:
        model = CloserUser
        fields = (
            "first_name",
            "second_name",
            "last_name",
            "email",
            "password",
            # "username",
            "phone_number",
            "date_of_birth",
            "current_city",
            "current_state",
            "current_country",
            "home_city",
            "home_state",
            "home_country",
            "profile_picture_url",
            "background_picture_url",
            "about_me",
            "education",
            "religion",
            "relationship",
            "gender",
        )
        labels = {
            "first_name": "",
            "second_name": "",
            "last_name": "",
            "email": "",
            "password": "",
            # "username",
            "phone_number": "",
            "date_of_birth": "",
            "current_city": "",
            "current_state": "",
            "current_country": "",
            "home_city": "",
            "home_state": "",
            "home_country": "",
            "profile_picture_url": "",
            "background_picture_url": "",
            "about_me": "",
            "education": "",
            "religion": "",
            "relationship": "",
            "gender": "",
        }
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "placeholder": "First name*",
                    "name": "first_name",
                    "class": "from-element",
                }
            ),
            "second_name": forms.TextInput(
                attrs={
                    "placeholder": "Second name",
                    "name": "second_name",
                    "class": "from-element",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "placeholder": "Last name*",
                    "name": "last_name",
                    "class": "from-element",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Email*",
                    "name": "email",
                    "class": "from-element",
                }
            ),
            "password": forms.PasswordInput(
                attrs={
                    "placeholder": "Password*",
                    "name": "password",
                    "class": "from-element",
                }
            ),
            # TODO: Specify or not the username
            # "username": forms.TextInput(
            #     attrs={
            #         "placeholder": "Username",
            #         "name": "username",
            #         "class": "from-element",
            #     }
            # ),
            "phone_number": forms.TextInput(
                attrs={
                    "placeholder": "Phone number",
                    "name": "phone_number",
                    "class": "from-element",
                }
            ),
            "date_of_birth": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={
                    "placeholder": "Date of birth*",
                    "name": "date_of_birth",
                    "type": "date",
                    "class": "form-element",
                },
            ),
            "current_city": forms.TextInput(
                attrs={
                    "placeholder": "Current city",
                    "name": "current_city",
                    "class": "from-element",
                }
            ),
            "current_state": forms.TextInput(
                attrs={
                    "placeholder": "Current state",
                    "name": "current_state",
                    "class": "from-element",
                }
            ),
            "current_country": forms.TextInput(
                attrs={
                    "placeholder": "Current country",
                    "name": "current_country",
                    "class": "from-element",
                }
            ),
            "home_city": forms.TextInput(
                attrs={
                    "placeholder": "Home city",
                    "name": "home_city",
                    "class": "from-element",
                }
            ),
            "home_state": forms.TextInput(
                attrs={
                    "placeholder": "Home state",
                    "name": "home_state",
                    "class": "from-element",
                }
            ),
            "home_country": forms.TextInput(
                attrs={
                    "placeholder": "Home country",
                    "name": "home_country",
                    "class": "from-element",
                }
            ),
            "about_me": forms.TextInput(
                attrs={
                    "placeholder": "About me",
                    "name": "about_me",
                    "class": "from-element",
                }
            ),
            "education": forms.TextInput(
                attrs={
                    "placeholder": "Education",
                    "name": "education",
                    "class": "from-element",
                }
            ),
        }
