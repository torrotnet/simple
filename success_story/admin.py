from django.contrib import admin

# Register your models here.
from .models import SuccessStory

class SuccessStoryAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "story_author", "story_timestamp_created"]

    class Meta:
        model = SuccessStory


admin.site.register(SuccessStory, SuccessStoryAdmin)
