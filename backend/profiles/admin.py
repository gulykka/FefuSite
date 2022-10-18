from django.contrib import admin

from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'phone_number',)
    list_display_links = ('id', 'username',)


class PublicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'character', 'category', 'content', 'created_at', 'update_at', 'photo', 'reaction')
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


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['user', 'created', 'updated']
    list_filter = ['created', 'updated']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Building, BuildingsAdmin)
admin.site.register(Service, ServiceAdmin)
