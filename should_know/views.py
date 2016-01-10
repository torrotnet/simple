from django.shortcuts import render
from should_know.forms import PersonForm
from should_know.models import Person, Company, Portfolio


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
    portfolio = Portfolio.objects.filter(company=company).all()
    context = {
        "title": title,
        "company": company,
        "portfolio": portfolio,
    }

    return render(request, "should-know-company-show.html", context)


def should_know_person_new(request):
    title = "Recommend person"
    form = PersonForm(request.POST or None)
    # specialities = Speciality.objects.all()
    # stack_skills = StackSkills.objects.all()
    context = {
        # "specialities": specialities,
        # "stack_skills": stack_skills,
        "title": title,
        "form": form
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        # author = form.cleaned_data.get("author")
        # instance.author = author
        context = {
            "title": "You recommended person successfully. Thank you!"
        }
        return render(request, "should-know-person-new-thank-you.html", context)

    return render(request, "should-know-person-new.html", context)


def should_know_company_new(request):
    title = "Success story"
    form = PersonForm(request.POST or None)

    # specialities = Speciality.objects.all()
    # stack_skills = StackSkills.objects.all()
    context = {
        # "specialities": specialities,
        # "stack_skills": stack_skills,
        "title": title,
        "form": form
    }

    if form.is_valid():
        instance = form.save(commit=False)
        # author = form.cleaned_data.get("author")
        # instance.author = author
        instance.save()
        context = {
            "title": "Your story saved successfully. Thank you!"
        }

    return render(request, "should-know-person-new.html", context)
