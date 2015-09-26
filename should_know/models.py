from django.core.validators import RegexValidator
from django.db import models


class Contact(models.Model):
    email = models.EmailField(max_length=254)
    skype = models.CharField(max_length=100)
    twitter = models.URLField()
    facebook = models.URLField()
    vk = models.URLField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    tel = models.CharField(max_length=16, validators=[phone_regex], blank=True)

    def __unicode__(self):
        return self.id

    class Meta:
        ordering = ('id',)


class Person(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField()
    contact = models.OneToOneField(Contact, primary_key=True)
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
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField()
    contact = models.OneToOneField(Contact, primary_key=True)
    link = models.URLField()
    location = models.CharField(max_length=100)
    stack_technology = models.ManyToManyField(StackTechnology)
    product_direction = models.ManyToManyField(ProductDirection)
    price_min = models.IntegerField()
    price_max = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('updated',)


class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    description = models.TextField()
    stack_technology = models.ManyToManyField(StackTechnology)
    product_direction = models.ManyToManyField(ProductDirection)
    company = models.ForeignKey(Company)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
