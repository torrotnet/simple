from django.shortcuts import render
from success_story.forms import SuccessStoryForm


def success_story(request):
    title = "Success story"
    form = SuccessStoryForm(request.POST or None)
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

    return render(request, "base.html", context)


def home(request):
    return render(request, "home.html", {})
