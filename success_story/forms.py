from django import forms
from .models import SuccessStory


class SuccessStoryForm(forms.ModelForm):

    class Meta:
        model = SuccessStory
        fields = ["title", "text", "author", "img_avatar", "img_background", "advice", "stack_skills", "used_to",
                  "became", "rate"]
