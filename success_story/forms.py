from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import SuccessStory, Speciality, StackSkills, Advice


# class SuccessStoryTextForm(forms.ModelForm):
#
#     class Meta:
#         model = SuccessStory
#         fields = ["text"]
#         widgets = {
#             # 'text': SummernoteWidget(attrs={'width': '100%', 'height': '500px'}),
#             'text': SummernoteInplaceWidget(attrs={'width': '100%', 'height': '500px'}),
#         }


class SuccessStoryForm(forms.ModelForm):

    class Meta:
        model = SuccessStory
        fields = ["title", "text", "author",
                  # "img_avatar", "img_background",
                  "stack_skills", "used_to", "became"]
        widgets = {
            'text': SummernoteWidget(attrs={'width': '100%', 'height': '500px'}),
            # 'text': SummernoteInplaceWidget(attrs={'width': '100%', 'height': '500px'}),
        }

    def clean_author(self):
        r = self.cleaned_data.get("author")
        if not r:
            r = "Unknown author"
        return r

    def clean_title(self):
        print self.cleaned_data.get("title")
        return self.cleaned_data.get("title") or "Unknown title"

    def clean_text(self):
        print self.cleaned_data.get("text")
        return self.cleaned_data.get("text") or "Unknown text"

    # def clean_stack_skills(self):
    #     print self.cleaned_data.get("stack_skills")
    #     return self.cleaned_data.get("stack_skills") or "1"





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
