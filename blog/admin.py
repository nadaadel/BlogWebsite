from django.contrib import admin
from .models import Post


# register the models

class CustomPost(admin.ModelAdmin):
    fieldsets = (["Personal_Information", {"fields": ["title", "description" ,"photo","rate","likes","dislikes","date","author"]}],  )








admin.site.register(Post, CustomPost)

