from django.contrib import admin

# Register your models here.

from . models import Category, Product
# We need to register this models for our admin page, so we could see them there Here we are also pre-populating are
# slug field with the name we entered for the category or product we will create. That way also making sure they are
# the same
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title',)}

