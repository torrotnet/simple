from django.contrib import admin

from .forms import SuccessStoryForm
from .models import SuccessStory

class SuccessStoryAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "story_author", "story_timestamp_created"]
    form = SuccessStoryForm
    # class Meta:
    #     model = SuccessStory


admin.site.register(SuccessStory, SuccessStoryAdmin)
