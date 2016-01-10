from django import forms
from django.forms import TextInput
from .models import StackTechnology, ProductDirection, Person, Company, Portfolio


# class ContactForm(forms.ModelForm):
#
#     class Meta:
#         model = Contact
#         fields = ["email", "skype", "twitter", "facebook", "vk", "tel"]


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ["name", "description", "photo",
                  "email", "skype", "twitter", "facebook", "vk", "tel", "location",
                  # "contact",
                  # "created", "updated"
                  ]
        widgets = {
            'title': TextInput(attrs={'class': 'textinput textInput form-control', 'placeholder': 'Story title...'}),
            'author': TextInput(attrs={'class': 'textinput textInput form-control', 'placeholder': 'Story author...'}),
            'advice': TextInput(attrs={'class': 'textinput textInput form-control', 'placeholder': 'My advice...'}),
        }



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
        fields = ["name", "description", "logo",
                  "email", "skype", "twitter", "facebook", "vk", "tel", "location",
                  # "contact",
                  "link", "stack_technology",
                  "product_direction", "price_min", "price_max",
                  # "created", "updated"
                  ]


class PortfolioForm(forms.ModelForm):

    class Meta:
        model = Portfolio
        fields = ["name", "link", "description", "stack_technology", "product_direction", "company"]

