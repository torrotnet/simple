from django.shortcuts import render


def should_know_list(request):
    title = "Should know"

    context = {
        "title": title,
    }

    return render(request, "should-know-list.html", context)