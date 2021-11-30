from django.contrib import admin

# Register your models here.
from articleapp.models import Article




@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'created_at', 'project', 'writer' ]
    list_display_links = ['title']
    list_filter = ['project']
    list_per_page = 30
    list_editable= ['project']