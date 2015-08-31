from django.shortcuts import render

# Create your views here.

def success_story(request):
    return render(request, "success_story.html", {})
