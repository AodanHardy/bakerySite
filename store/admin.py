from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Product, Order, OrderItem

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'image_thumbnail')  # Add 'image_thumbnail' here
    search_fields = ('name', 'description')
    readonly_fields = ('image_thumbnail',)  # Add this line

    def image_thumbnail(self, obj):
        return obj.image.url if obj.image else ''

    image_thumbnail.short_description = 'Thumbnail'  # Add this line



admin.site.register(Product, ProductAdmin)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date_ordered', 'status')
    list_filter = ('status',)
    search_fields = ('user__username',)
    inlines = (OrderItemInline,)

admin.site.register(Order, OrderAdmin)
