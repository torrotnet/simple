from django.contrib import admin

from .forms import SuccessStoryForm, SpecialityForm, StackSkillsForm
from .models import SuccessStory, Speciality, StackSkills


class SuccessStoryAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "author", "created"]
    form = SuccessStoryForm
    # class Meta:
    #     model = SuccessStory

class SpecialityAdmin(admin.ModelAdmin):
    list_display = ["__unicode__"]
    form = SpecialityForm


class StackSkillsAdmin(admin.ModelAdmin):
    list_display = ["__unicode__"]
    form = StackSkillsForm

admin.site.register(SuccessStory, SuccessStoryAdmin)
admin.site.register(Speciality, SpecialityAdmin)
admin.site.register(StackSkills, StackSkillsAdmin)
