from django.shortcuts import render
from .models import Person, Company


def should_know_list(request):
    title = "Should know"
    persons = Person.objects.all()
    companies = Company.objects.all()
    context = {
        "title": title,
        "persons": persons,
        "companies": companies
    }

    return render(request, "should-know-list.html", context)


def should_know_person(request, id):
    title = "Should know"
    person = Person.objects.filter(contact_id=id).first()
    context = {
        "title": title,
        "person": person,
    }

    return render(request, "should-know-person-show.html", context)


def should_know_company(request, id):
    title = "Should know"
    company = Company.objects.filter(contact_id=id).first()
    context = {
        "title": title,
        "company": company,
    }

    return render(request, "should-know-company-show.html", context)
