from django.contrib import admin

from cart.models import Cart, CartItem

class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'date_added')

class CartItemtAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity', 'is_active', 'id')

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemtAdmin)
# Register your models here.
