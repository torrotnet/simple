from django.contrib import admin

from .forms import SuccessStoryForm, SpecialityForm, StackSkillsForm, AdviceForm
from .models import SuccessStory, Speciality, StackSkills, Advice


class SuccessStoryAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "author",
                    # "advice",
                    "used_to", "became", "rate", "created", "updated"]
    form = SuccessStoryForm
    # class Meta:
    #     model = SuccessStory


class SpecialityAdmin(admin.ModelAdmin):
    list_display = ["__unicode__"]
    form = SpecialityForm


class StackSkillsAdmin(admin.ModelAdmin):
    list_display = ["__unicode__"]
    form = StackSkillsForm


class AdviceAdmin(admin.ModelAdmin):
    list_display = ["__unicode__"]
    form = AdviceForm


admin.site.register(SuccessStory, SuccessStoryAdmin)
admin.site.register(Speciality, SpecialityAdmin)
admin.site.register(StackSkills, StackSkillsAdmin)
admin.site.register(Advice, AdviceAdmin)
