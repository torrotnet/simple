from django import forms
from .models import Contact, Person, StackTechnology, ProductDirection, Company, Portfolio


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ["email", "skype", "twitter", "facebook", "vk", "tel"]


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ["name", "description", "photo", "contact",
                  # "created", "updated"
                  ]


class StackTechnologyForm(forms.ModelForm):

    class Meta:
        model = StackTechnology
        fields = ["technology"]


class ProductDirectionForm(forms.ModelForm):

    class Meta:
        model = ProductDirection
        fields = ["direction"]


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ["name", "description", "logo", "contact", "link", "location", "stack_technology",
                  "product_direction", "price_min", "price_max",
                  # "created", "updated"
                  ]


class PortfolioForm(forms.ModelForm):

    class Meta:
        model = Portfolio
        fields = ["name", "link", "description", "stack_technology", "product_direction", "company"]

