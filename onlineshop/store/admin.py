from django.contrib import admin

from store.models import Products, Variation


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('product_name',)}
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available', 'id',)

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active', )
    list_filter = ('product', 'variation_category')

admin.site.register(Products, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
# Register your models here.
