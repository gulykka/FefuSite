from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'phone_number',)
    list_display_links = ('id', 'username',)

class PublicatonAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'character', 'category', 'content', 'created_at', 'update_at', 'photo',)
    list_display_links = ('id', 'author')
    search_fields = ('content',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')


class BuildingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Publication, PublicatonAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Building, BuildingsAdmin)
