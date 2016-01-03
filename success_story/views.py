from django.shortcuts import render
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
    # if request.POST:
    #     form["author"] = form.clean_author()

    if form.is_valid():
        instance = form.save(commit=False)
        # author = form.cleaned_data.get("author")
        # instance.author = author
        instance.save()
        # form["author"] = form.clean_author()
        context = {
            "title": "Your story saved succesfully. Thank you!",
            # "form": form
        }

    return render(request, "storylist.html", context)


def success_story(request, id):
    title = "Success story"
    story = SuccessStory.objects.filter(id=id).first()

    context = {
        "title": title,
        "story": story,
    }
    return render(request, "story-show.html", context)


def success_story_new(request):
    title = "Success story"

    form = SuccessStoryForm(request.POST or None)
    specialities = Speciality.objects.all()
    stack_skills = StackSkills.objects.all()
    context = {
        "specialities": specialities,
        "stack_skills": stack_skills,
        "title": title,
        "form": form
    }
    print(form.is_valid())
    if form.is_valid():
        # form.save()
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        # author = form.cleaned_data.get("author")
        # instance.author = author
        # instance.save()
        context = {
            "title": "Your story saved succesfully. Thank you!"
        }
        return render(request, "success_story_new_thank_you.html", context)

    return render(request, "success-story-new.html", context)


def success_story_new_thank_you(request):
    title = "Success story saved"
    context = {
        "title": title,
    }
    return render(request, "success_story_new_thank_you.html", context)


def home(request):
    return render(request, "home.html", {})
