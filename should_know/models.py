from django.core.validators import RegexValidator
from django.db import models


# class Contact(models.Model):
#     # email = models.EmailField(max_length=254, blank=True, null=True)
#     # skype = models.CharField(max_length=100, blank=True, null=True)
#     # twitter = models.URLField(blank=True, null=True)
#     # facebook = models.URLField(blank=True, null=True)
#     # vk = models.URLField(blank=True, null=True)
#     # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
#     # tel = models.CharField(max_length=16, validators=[phone_regex], blank=True, null=True)
#
#     def __unicode__(self):
#         return "%s" % self.id
#
#     class Meta:
#         ordering = ('id',)


class Person(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=140)
    photo = models.ImageField(blank=True, null=True)
    # contact = models.OneToOneField(Contact, primary_key=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    skype = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    vk = models.URLField(blank=True, null=True)
    linked_in = models.URLField(blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    tel = models.CharField(max_length=16, validators=[phone_regex], blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('updated',)


class StackTechnology(models.Model):
    technology = models.CharField(max_length=100)

    def __unicode__(self):
        return self.technology

    class Meta:
        ordering = ('technology',)


class ProductDirection(models.Model):
    direction = models.CharField(max_length=100)

    def __unicode__(self):
        return self.direction

    class Meta:
        ordering = ('direction',)


class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    logo = models.ImageField(blank=True, null=True)
    # contact = models.OneToOneField(Contact, primary_key=True)
    link = models.URLField(blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    skype = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    vk = models.URLField(blank=True, null=True)
    linked_in = models.URLField(blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    tel = models.CharField(max_length=16, validators=[phone_regex], blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    stack_technology = models.ManyToManyField(StackTechnology)
    product_direction = models.ManyToManyField(ProductDirection)
    price_min = models.IntegerField(blank=True, null=True)
    price_max = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('updated',)


class Portfolio(models.Model):
    name_portfolio = models.CharField(max_length=100)
    link_portfolio = models.URLField(blank=True, null=True)
    description_portfolio = models.TextField()
    stack_technology_portfolio = models.ManyToManyField(StackTechnology)
    product_direction_portfolio = models.ManyToManyField(ProductDirection)
    company_portfolio = models.ForeignKey(Company, blank=True)

    def __unicode__(self):
        return self.name_portfolio

    class Meta:
        ordering = ('-id',)
