from django import forms

from .models import Post, Poll, Test, Short


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "description", "image")
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Post title*",
                    "name": "title",
                    "class": "post-title",
                }
            ),
            "description": forms.TextInput(
                attrs={
                    "placeholder": "Post description*",
                    "name": "description",
                    "class": "post-description",
                }
            ),
        }


class PollFrom(forms.ModelForm):
    class Meta:
        model = Poll
        fields = (
            "title",
            "question",
            "first_ans",
            "second_ans",
            "third_ans",
            "fourth_ans",
        )
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Poll title*",
                    "name": "title",
                    "class": "poll-title",
                }
            ),
            "question": forms.TextInput(
                attrs={
                    "placeholder": "Poll question*",
                    "name": "question",
                    "class": "poll-question",
                }
            ),
            "first_ans": forms.TextInput(
                attrs={
                    "placeholder": "First answer*",
                    "name": "first_ans",
                    "class": "poll-first_ans",
                }
            ),
            "second_ans": forms.TextInput(
                attrs={
                    "placeholder": "Second answer*",
                    "name": "second_ans",
                    "class": "poll-second_ans",
                }
            ),
            "third_ans": forms.TextInput(
                attrs={
                    "placeholder": "Third answer*",
                    "name": "third_ans",
                    "class": "poll-third_ans",
                }
            ),
            "fourth_ans": forms.TextInput(
                attrs={
                    "placeholder": "Fourth answer*",
                    "name": "fourth_ans",
                    "class": "poll-fourth_ans",
                }
            ),
        }


class TestFrom(forms.ModelForm):
    class Meta:
        model = Test
        fields = (
            "title",
            "question",
            "first_ans",
            "second_ans",
            "third_ans",
            "fourth_ans",
            "correct_ans",
        )
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Test title*",
                    "name": "title",
                    "class": "test-title",
                }
            ),
            "question": forms.TextInput(
                attrs={
                    "placeholder": "Test question*",
                    "name": "question",
                    "class": "test-question",
                }
            ),
            "first_ans": forms.TextInput(
                attrs={
                    "placeholder": "First answer*",
                    "name": "first_ans",
                    "class": "test-first_ans",
                }
            ),
            "second_ans": forms.TextInput(
                attrs={
                    "placeholder": "Second answer*",
                    "name": "second_ans",
                    "class": "test-second_ans",
                }
            ),
            "third_ans": forms.TextInput(
                attrs={
                    "placeholder": "Third answer*",
                    "name": "third_ans",
                    "class": "test-third_ans",
                }
            ),
            "fourth_ans": forms.TextInput(
                attrs={
                    "placeholder": "Fourth answer*",
                    "name": "fourth_ans",
                    "class": "test-fourth_ans",
                }
            ),
            "correct_ans": forms.TextInput(
                attrs={
                    "placeholder": "Correct answer*",
                    "name": "correct_ans",
                    "class": "test-correct_ans",
                }
            ),
        }


class ShortForm(forms.ModelForm):
    class Meta:
        model = Short
        fields = ("title", "video")
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Short title*",
                    "name": "title",
                    "class": "short-title",
                }
            )
        }

