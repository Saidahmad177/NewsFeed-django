from django.contrib import admin
from firstapp.models import NewsBase, Category, Contact, AllUser, Comments


# @admin.register(NewsBase)
class NewsBaseModel(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_time', 'category', 'status']
    list_filter = ['title', 'created_time', 'status']
    prepopulated_fields = {'slug': ('title', )}
    date_hierarchy = 'created_time'
    search_fields = ['title', 'id']
    ordering = ['status', 'created_time']


admin.site.register(NewsBase, NewsBaseModel)


# @admin.register(Category)
class CategoryModel(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Category, CategoryModel)


# @admin.register(Contact)
class ContactModel(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']


admin.site.register(Contact, ContactModel)


class UserModel(admin.ModelAdmin):
    list_display = ['username', 'email']


admin.site.register(AllUser, UserModel)


class CommentModel(admin.ModelAdmin):
    list_display = ['user', 'created_time', 'active']
    list_filter = ['created_time', 'active']
    search_fields = ['user', 'body']
    actions = ['disable_comments', 'enable_comments']

    def disable_comments(self, request, queryset):
        return queryset.update(active=False)

    def enable_comments(self, request, queryset):
        return queryset.update(active=True)


admin.site.register(Comments, CommentModel)
