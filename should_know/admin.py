from django.contrib import admin
from should_know.forms import StackTechnologyForm, ProductDirectionForm, PersonForm, CompanyForm, PortfolioForm
from should_know.models import StackTechnology, ProductDirection, Person, Company, Portfolio


# class ContactAdmin(admin.ModelAdmin):
#     list_display = ["__unicode__", "skype", "twitter", "facebook", "vk", "tel"]
#     form = ContactForm


class PersonAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "description", "photo",
                    "email", "skype", "twitter", "facebook", "vk", "linked_in", "tel", "location",
                    # "contact",
                    "created", "updated"]
    form = PersonForm


class StackTechnologyAdmin(admin.ModelAdmin):
    list_display = ["__unicode__"]
    form = StackTechnologyForm


class ProductDirectionAdmin(admin.ModelAdmin):
    list_display = ["__unicode__"]
    form = ProductDirectionForm


class CompanyAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "description", "logo",
                    "email", "skype", "twitter", "facebook", "vk", "tel", "location",
                    # "contact",
                    "link", "location", "price_min", "price_max", "created", "updated"]
    form = CompanyForm


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "link", "description", "company"]
    form = PortfolioForm

admin.site.register(Person, PersonAdmin)
admin.site.register(StackTechnology, StackTechnologyAdmin)
admin.site.register(ProductDirection, ProductDirectionAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
