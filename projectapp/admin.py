from django.contrib import admin

# Register your models here.
from projectapp.models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'created_at']
    list_display_links = ['title']

admin.site.register(Project, ProjectAdmin)