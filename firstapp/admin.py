from django.contrib import admin
from firstapp.models import NewsBase, Category, Contact, AllUser


@admin.register(NewsBase)
class NewsBase(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_time', 'category', 'status']
    list_filter = ['title', 'created_time', 'status']
    prepopulated_fields = {'slug': ('title', )}
    date_hierarchy = 'created_time'
    search_fields = ['title', 'id']
    ordering = ['status', 'created_time']


# @admin.register(Category)
class CategoryModel(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Category, CategoryModel)


@admin.register(Contact)
class ContactModel(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']


class Usermodel(admin.ModelAdmin):
    list_display = ['username', 'email']


admin.site.register(AllUser, Usermodel)
