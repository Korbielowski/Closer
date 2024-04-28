from django import forms

from .models import Post


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
