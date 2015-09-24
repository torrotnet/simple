from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import SuccessStory, Speciality, StackSkills, Advice


class SuccessStoryForm(forms.ModelForm):

    class Meta:
        model = SuccessStory
        fields = ["title", "text", "author", "img_avatar", "img_background", "stack_skills", "used_to", "became"]
        # widgets = {
        #     'text': SummernoteWidget(attrs={'width': '50%', 'height': '500px'}),
        #     # 'text': SummernoteInplaceWidget(),
        # }


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
