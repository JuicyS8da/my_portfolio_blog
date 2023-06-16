from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *

class PostAdmin(ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class WorkAdmin(ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.register(PostTags, CategoryAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(WorkTags, CategoryAdmin)
admin.site.register(Resume)
admin.site.register(About)
