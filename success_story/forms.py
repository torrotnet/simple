from django import forms
from django.core.exceptions import ValidationError
from django.forms import TextInput, Select, Textarea, FileInput, ClearableFileInput, HiddenInput, SelectMultiple
from django.utils.encoding import smart_unicode
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import SuccessStory, Speciality, StackSkills


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
                  "advice",
                  # "img_avatar",
                  # "img_background",
                  "stack_skills",
                  "used_to", "became"
                  ]
        widgets = {
            # 'text': SummernoteWidget(attrs={'width': '100%', 'height': '500px'}),
            # 'text': SummernoteInplaceWidget(attrs={'width': '100%', 'height': '500px'}),
            'title': TextInput(attrs={'class': 'textinput textInput form-control', 'placeholder': 'Story title...', 'autofocus': 'autofocus'}),
            'author': TextInput(attrs={'class': 'textinput textInput form-control', 'placeholder': 'Story author...'}),
            'advice': TextInput(attrs={'class': 'textinput textInput form-control', 'placeholder': 'My advice...'}),

            'used_to': Select(attrs={'class': 'chosen-select', 'style': 'min-width: 265px', 'tabindex': '0'}),
            'became': Select(attrs={'class': 'chosen-select', 'style': 'min-width: 265px', 'tabindex': '0'}),

            'stack_skills': SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 265px',
                                                  'tabindex': '0',
                                                  'data-placeholder': "Select skills..."}),
            'text': Textarea(attrs={'class': 'summernote', 'required': 'True'}),
            # 'img_avatar': TextInput(attrs={
                # "class": "dropzone"
                # 'class': 'dropzone dz-clickable'
            # })

        }

    def __init__(self, *args, **kwargs):
        super(SuccessStoryForm, self).__init__(*args, **kwargs)
        self.fields['used_to'].empty_label = "I used to work as (position)..."
    #    # following line needed to refresh widget copy of choice list
        # self.fields['used_to'].widget.choices = self.fields['used_to'].choices
        self.fields['became'].empty_label = "I am working  now (position)..."
        # self.fields['became'].widget.choices = self.fields['became'].choices
        self.fields['stack_skills'].empty_label = "Select using skills..."
        # self.fields['stack_skills'].widget.choices = self.fields['stack_skills'].choices

    # def clean_author(self):
    #     r = self.cleaned_data.get("author")
    #     if not r:
    #         r = "Unknown author"
    #     return r
    #
    # def clean_title(self):
    #     print self.cleaned_data.get("title")
    #     return self.cleaned_data.get("title") or "Unknown title"
    #
    # def clean_text(self):
    #     print self.cleaned_data.get("text")
    #     return self.cleaned_data.get("text") or "Unknown text"

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


# class AdviceForm(forms.ModelForm):
#
#     class Meta:
#         model = Advice
#         fields = ["text"]
