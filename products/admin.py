from django.contrib import admin
from . models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    search_fields = ['title', 'description']
    list_filter = ['price', 'active']
    list_display = ['__str__', 'title','price','active', 'updated']
    list_editable = ['price','active']
    readonly_fields = ['timestamp','updated']
    prepopulated_fields = {"slug": ("title", )}

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)