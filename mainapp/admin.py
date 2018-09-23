from django.contrib import admin

from .models import Author, PageContent, Tags

admin.site.register(Author)
admin.site.register(PageContent)
admin.site.register(Tags)

