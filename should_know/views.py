from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext
from .models import Person, Company, Portfolio, StackTechnology, ProductDirection
from should_know.forms import PersonForm, CompanyForm, PortfolioForm


def should_know_list(request):
    title = "Should know"
    persons = Person.objects.all().order_by('-updated')
    companies = Company.objects.all().order_by('-updated')
    context = {
        "title": title,
        "persons": persons,
        "companies": companies
    }

    return render(request, "should-know-list.html", context)


def should_know_person(request, id):
    title = "Should know"
    person = Person.objects.filter(id=id).first()
    context = {
        "title": title,
        "person": person,
    }

    return render(request, "should-know-person-show.html", context)


def should_know_company(request, company_id):
    title = "Should know"
    company = Company.objects.filter(id=company_id).first()
    portfolio = Portfolio.objects.filter(company_portfolio=company).all()
    add_project_form = PortfolioForm()
    context = {
        "title": title,
        "company": company,
        "portfolio": portfolio,
        "add_project_form": add_project_form
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


def should_know_company_edit(request, company_id=None, template_name='should-know-company-new.html'):
    if company_id:
        company = get_object_or_404(Company, pk=company_id)
        title = "Edit company info"
        context = {"company_id": company_id}
        # if company.author != request.user:   # uncomment when authorisation is in project
        #     return HttpResponseForbidden()
    else:
        company = Company(
            # author=request.user              # uncomment when authorisation is in project
            )
        title = "Recommend company"
        context = {}

    form = CompanyForm(request.POST or None, instance=company)
    if request.POST:
        if form.is_valid():
            instance = form.save(commit=False)
            company_name = instance.name
            instance.save()
            form.save_m2m()

            # If the save was successful, redirect to another page
            if not company_id:
                company_id = Company.objects.get(name=company_name).id
            redirect_url = reverse(should_know_company, kwargs={'company_id': company_id})
            return HttpResponseRedirect(redirect_url)

    context.update({'form': form,
                    'title': title,
                    })
    return render_to_response(template_name, context, context_instance=RequestContext(request))


def add_project_to_portfolio(request, company_id):
    form = PortfolioForm(request.POST or None)
    company = Company.objects.get(id=company_id)
    if form.is_valid:
        instance = form.save(commit=False)
        instance.company_portfolio = company
        instance.save()
        form.save_m2m()
        redirect_url = reverse(should_know_company, kwargs={'company_id': company_id})
        return HttpResponseRedirect(redirect_url)
    return HttpResponseRedirect('/should-know/company/edit/%i/' % int(company_id))

def delete_project_from_portfolio(company_id, project_id):
    project = get_object_or_404(Portfolio, pk=project_id)
    project.delete()
    redirect_url = reverse(should_know_company, kwargs={'company_id': company_id})
    return HttpResponseRedirect(redirect_url)
