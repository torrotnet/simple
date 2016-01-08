from django.db import models


class StackSkills(models.Model):
    skill = models.CharField(max_length=100)

    def __unicode__(self):
        return self.skill

    class Meta:
        ordering = ('skill',)


class Speciality(models.Model):
    spec_title = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.spec_title

    class Meta:
        ordering = ('spec_title',)


class SuccessStory(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.CharField(max_length=100)
    advice = models.CharField(max_length=140, default='')
    img_avatar = models.ImageField(null=True, blank=True)
    img_background = models.ImageField(null=True, blank=True)
    stack_skills = models.ManyToManyField(StackSkills)
    used_to = models.ForeignKey(Speciality, related_name='succ_used_to')
    became = models.ForeignKey(Speciality, related_name='succ_became')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    rate = models.DecimalField(max_digits=3, decimal_places=1, default=0)

    def __unicode__(self):
        return self.title


# class Advice(models.Model):
#     success_story = models.ForeignKey(SuccessStory)
#     text = models.CharField(max_length=200)
#
#     def __unicode__(self):
#         return "Advices for %s story" % self.id
