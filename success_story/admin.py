from django.contrib import admin

from .forms import SuccessStoryForm
from .models import SuccessStory


class SuccessStoryAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "author", "created"]
    form = SuccessStoryForm
    # class Meta:
    #     model = SuccessStory


admin.site.register(SuccessStory, SuccessStoryAdmin)
