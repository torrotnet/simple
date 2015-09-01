from django import forms
from .models import SuccessStory

class SuccessStoryForm(forms.ModelForm):
    class Meta:
        model = SuccessStory
        fields = ["story_title", "story_text", "story_author", "story_img_avatar", "story_img_background",
                  "story_advice", "story_stack", "story_used_to", "story_became", "story_rate"]
