from django.contrib import admin



# Register your models here.

from .models import Category, SubCategory


class SubcategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 0
    readonly_fields = ('slug',)

class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubcategoryInline]
    readonly_fields=('slug',)

admin.site.register(Category, CategoryAdmin)
