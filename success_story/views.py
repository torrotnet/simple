from django.shortcuts import render
from django import forms
from success_story.forms import SuccessStoryForm
from success_story.models import SuccessStory, Speciality, StackSkills


def success_story_list(request):
    title = "Success story"
    form = SuccessStoryForm(request.POST or None)
    stories = SuccessStory.objects.all()
    context = {
        "title": title,
        "form": form,
        "stories": stories
    }

    if form.is_valid():
        instance = form.save(commit=False)
        # author = form.cleaned_data.get("author")
        # instance.author = author
        instance.save()
        context = {
            "title": "Your story saved succesfully. Thank you!"
        }

    return render(request, "storylist.html", context)


def success_story(request, id):
    title = "Success story"
    story = SuccessStory.objects.filter(id=id).first()
    context = {
        "title": title,
        "story": story,
    }
    return render(request, "story_show.html", context)


def success_story_new(request):
    title = "Success story"
    spec = [(spec.spec_title, spec.spec_title) for spec in Speciality.objects.all()]
    stack_skills_choices = [(ss.skill, ss.skill) for ss in StackSkills.objects.all()]

    # used_to = forms.ChoiceField(required=True, label='Project creator', choices=spec)

    form = SuccessStoryForm(request.POST or None)

    form.fields["used_to"].choices = spec
    form.fields["became"].choices = spec
    form.fields["stack_skills"].choices = stack_skills_choices

    context = {
        "title": title,
        "form": form
    }

    if form.is_valid():
        instance = form.save(commit=False)
        # author = form.cleaned_data.get("author")
        # instance.author = author
        instance.save()
        context = {
            "title": "Your story saved succesfully. Thank you!"
        }

    return render(request, "success_story_new.html", context)


def success_story_new_thank_you(request):
    title = "Success story saved"
    context = {
        "title": title,
    }
    return render(request, "success_story_new_thank_you.html", context)


def home(request):
    return render(request, "home.html", {})
