from django.contrib import admin
from .models import post
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = 'body'

admin.site.register(post, PostAdmin)