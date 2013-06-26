from categories.models import Category
from django.contrib import admin

class CategoryAdmin(admin.ModelAdmin):
    excluded = ('slug',)

admin.site.register(Category, CategoryAdmin)
