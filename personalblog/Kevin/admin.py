from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
# admin.site.register(KevinPost)
# admin.site.register(KevinComment)

@admin.register(KevinPost)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'content', 'publication_date')
    search_fields = ('user', 'title')
    list_filter = ('title',  'user')

@admin.register(KevinComment)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'content', 'timestamp')
    search_fields = ('user', 'post')
    list_filter = ('post',  'user')
