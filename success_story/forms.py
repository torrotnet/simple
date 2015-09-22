from django import forms
from .models import SuccessStory, Speciality, StackSkills, Advice


class SuccessStoryForm(forms.ModelForm):
    # spec = [(spec.spec_title, spec.spec_title) for spec in Speciality.objects.all()]
    # stack_skills_choices = [(ss.skill, ss.skill) for ss in StackSkills.objects.all()]
    #
    # stack_skills = forms.MultipleChoiceField(required=True, choices=stack_skills_choices)
    # used_to = forms.ChoiceField(required=True, choices=spec)
    # became = forms.ChoiceField(required=True, choices=spec)

    class Meta:
        model = SuccessStory
        fields = ["title", "text", "author", "img_avatar", "img_background", "stack_skills", "used_to",
                  "became"]


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
