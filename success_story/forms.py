from django import forms
from .models import SuccessStory, Speciality, StackSkills, Advice


class SuccessStoryForm(forms.ModelForm):

    class Meta:
        model = SuccessStory
        fields = ["title", "text", "author", "img_avatar", "img_background", "stack_skills", "used_to", "became"]


class StackSkillsForm(forms.ModelForm):

    class Meta:
        model = StackSkills
        fields = ["skill"]


class SpecialityForm(forms.ModelForm):

    class Meta:
        model = Speciality
        fields = ["spec_title"]


class AdviceForm(forms.ModelForm):

    class Meta:
        model = Advice
        fields = ["text"]
