from django.contrib import admin

# Register your models here.
from snippets.models import Snippet
@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ['id','created','title','code','linenos','language','style']

