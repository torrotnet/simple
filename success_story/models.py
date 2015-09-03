from django.db import models


MY_CHOICES = ((1, "Flask"), (2, "Django"),)

class StackSkills(models.Model):
    skill = models.CharField(max_length=100)

    def __unicode__(self):
        return self.skill

    class Meta:
        ordering = ('skill',)


class SuccessStory(models.Model):
    story_title = models.CharField(max_length=100)
    story_text = models.TextField()
    story_author = models.CharField(max_length=100)
    story_img_avatar = models.ImageField(null=True, blank=True)
    story_img_background = models.ImageField(null=True, blank=True)
    story_advice = models.CharField(max_length=120)
    story_stack = models.ManyToManyField(StackSkills)
    story_used_to = models.CharField(max_length=100)
    story_became = models.CharField(max_length=100)
    story_timestamp_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    story_timestamp_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    story_rate = models.DecimalField(max_digits=3, decimal_places=1, default=0)

    def __unicode__(self):
        return self.story_title

