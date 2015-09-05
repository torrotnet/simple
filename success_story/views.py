from django.shortcuts import render


def success_story(request):
    return render(request, "success_story.html", {})


def home(request):
    return render(request, "home.html", {})
