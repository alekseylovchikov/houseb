from django.contrib import admin
from .models import Project
from .models import Contact


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'size', 'project_date', 'is_published', 'is_main_page', 'type')
    list_display_links = ('id', 'title')
    list_filter = ('size', 'type')
    list_editable = ('is_published', 'is_main_page')
    search_fields = ('title', 'description', 'size', 'price')
    list_per_page = 25


class ContactAdmin(admin.ModelAdmin):
    list_display = ('title', 'value')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Contact, ContactAdmin)
