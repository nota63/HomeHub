from django.contrib import admin

# Register your models here.
from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')


admin.site.register(Feedback, FeedbackAdmin)
