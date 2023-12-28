from django.contrib import admin
from .models import Category


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    # use for automatically add a slug when you create product
    prepopulated_fields = {"slug": ("category_name",)}
    list_display = ("category_name", "slug")


# register the model here in ordered to use in the admin pale
admin.site.register(Category,CategoryAdmin)
