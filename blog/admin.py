from django.contrib import admin
from .models import Post ,Tag


# register the models

class CustomPost(admin.ModelAdmin):
    fieldsets = (["Personal_Information", {"fields": ["title", "description" ,"photo","rate","likes","dislikes","date","author" ,"tag"]}],  )




class CustomTag(admin.ModelAdmin):
    fieldsets = (["Tags",{"fields": ["tag",]}],)



admin.site.register(Post, CustomPost)

admin.site.register(Tag, CustomTag)