from django import forms
from django.forms import TextInput, URLInput, EmailInput, SelectMultiple, NumberInput
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
                  "email", "skype", "linked_in", "twitter", "facebook", "vk", "tel", "location",
                  # "contact",
                  "link", "stack_technology", "product_direction", "price_min", "price_max",
                  # "created", "updated"
                  ]
        widgets = {
            'name': TextInput(attrs={'class': 'textinput textInput form-control border-color-focus', 'placeholder': 'Company full name...'}),
            'description': TextInput(attrs={'class': 'textinput textInput form-control border-color-focus', 'placeholder': 'About company...'}),
            'email': EmailInput(attrs={'class': 'textinput textInput form-control border-color-focus', 'placeholder': 'Email...'}),
            'link': URLInput(attrs={'class': 'textinput textInput form-control border-color-focus', 'placeholder': 'Company site...'}),
            'skype': TextInput(attrs={'class': 'textinput textInput form-control border-color-focus', 'placeholder': 'Skype...'}),
            'twitter': TextInput(attrs={'class': 'textinput textInput form-control border-color-focus', 'placeholder': 'Twitter...'}),
            'facebook': URLInput(attrs={'class': 'textinput textInput form-control border-color-focus', 'placeholder': 'Facebook...'}),
            'vk': URLInput(attrs={'class': 'textinput textInput form-control border-color-focus', 'placeholder': 'VK...'}),
            'linked_in': URLInput(attrs={'class': 'textinput textInput form-control border-color-focus', 'placeholder': 'Linked in...'}),
            'tel': TextInput(attrs={'class': 'textinput textInput form-control border-color-focus', 'placeholder': 'Telefone number...'}),
            'location': TextInput(attrs={'class': 'textinput textInput form-control border-color-focus', 'placeholder': 'Location...'}),
            'stack_technology': SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 265px',
                                                      'tabindex': '0',
                                                      'data-placeholder': "Select technologies..."}),
            'product_direction': SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 265px',
                                                       'tabindex': '0',
                                                       'data-placeholder': "Select directions..."}),
            'price_min': NumberInput(attrs={'class': 'textinput textInput form-control border-color-focus', 'placeholder': 'Min price...'}),
            'price_max': NumberInput(attrs={'class': 'textinput textInput form-control border-color-focus', 'placeholder': 'Max price...'}),

        }


class PortfolioForm(forms.ModelForm):

    class Meta:
        model = Portfolio
        fields = ["name_portfolio", "link_portfolio", "description_portfolio", "stack_technology_portfolio",
                  "product_direction_portfolio", "company_portfolio"]

        widgets = {
            'name_portfolio': TextInput(attrs={'class': 'textinput textInput form-control border-color-focus', 'placeholder': 'Project name...', 'style': 'width: 100%'}),
            'description_portfolio': TextInput(attrs={'class': 'textinput textInput form-control border-color-focus', 'placeholder': 'About project...', 'style': 'width: 100%'}),
            'link_portfolio': URLInput(attrs={'class': 'textinput textInput form-control border-color-focus', 'placeholder': 'Project site...', 'style': 'width: 100%'}),
            'stack_technology_portfolio': SelectMultiple(attrs={'class': 'chosen-select', 'style': 'width: 100%',
                                                      'tabindex': '0',
                                                      'data-placeholder': "Select technologies..."}),
            'product_direction_portfolio': SelectMultiple(attrs={'class': 'chosen-select', 'style': 'width: 100%',
                                                       'tabindex': '0',
                                                       'data-placeholder': "Select directions..."})
            }
