from django import forms
from django.forms import TextInput, URLInput, EmailInput
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
                  "email", "skype", "twitter", "facebook", "vk", "linked_in", "tel", "location",
                  # "contact",
                  # "created", "updated"
                  ]
        widgets = {
            'name': TextInput(attrs={'class': 'textinput textInput form-control border-color-focus', 'placeholder': 'Person full name...'}),
            'description': TextInput(attrs={'class': 'textinput textInput form-control border-color-focus', 'placeholder': 'About person...'}),
            'email': EmailInput(attrs={'class': 'textinput textInput form-control border-color-focus', 'placeholder': 'Email...'}),
            'skype': TextInput(attrs={'class': 'textinput textInput form-control border-color-focus', 'placeholder': 'Skype...'}),
            'twitter': TextInput(attrs={'class': 'textinput textInput form-control border-color-focus', 'placeholder': 'Twitter...'}),
            'facebook': URLInput(attrs={'class': 'textinput textInput form-control border-color-focus', 'placeholder': 'Facebook...'}),
            'vk': URLInput(attrs={'class': 'textinput textInput form-control border-color-focus', 'placeholder': 'VK...'}),
            'linked_in': URLInput(attrs={'class': 'textinput textInput form-control border-color-focus', 'placeholder': 'Linked in...'}),
            'tel': TextInput(attrs={'class': 'textinput textInput form-control border-color-focus', 'placeholder': 'Telefone number...'}),
            'location': TextInput(attrs={'class': 'textinput textInput form-control border-color-focus', 'placeholder': 'Location...'}),
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

