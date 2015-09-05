from django import forms
from .models import SuccessStory, Speciality, StackSkills



class SuccessStoryForm(forms.ModelForm):

    class Meta:
        model = SuccessStory
        fields = ["title", "text", "author", "img_avatar", "img_background", "advice", "stack_skills", "used_to",
                  "became", "rate"]


class StackSkillsForm(forms.ModelForm):

    class Meta:
        model = StackSkills
        fields = ["skill"]


class SpecialityForm(forms.ModelForm):

    class Meta:
        model = Speciality
        fields = ["title"]
