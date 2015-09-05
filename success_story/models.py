from django.db import models


MY_CHOICES = ((1, "Flask"), (2, "Django"),)

class StackSkills(models.Model):
    skill = models.CharField(max_length=100)

    def __unicode__(self):
        return self.skill

    class Meta:
        ordering = ('skill',)


class SuccessStory(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.CharField(max_length=100)
    img_avatar = models.ImageField(null=True, blank=True)
    img_background = models.ImageField(null=True, blank=True)
    advice = models.CharField(max_length=120)
    stack_skills = models.ManyToManyField(StackSkills)
    used_to = models.CharField(max_length=100)
    became = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    rate = models.DecimalField(max_digits=3, decimal_places=1, default=0)

    def __unicode__(self):
        return self.title

