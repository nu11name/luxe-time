from django.contrib import admin
from .models import (
    Product,
    Manufacturer,
    Category,
    Type,
    SpecialOffer,
    ProductImage,
    ProductDetails
)


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1

class ProductDetailsInline(admin.StackedInline):
    model = ProductDetails
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'old_price', 'category', 'type', 'position', 'condition', 'is_sale', 'views',
                    'image_tag']
    list_editable = ['category', 'type', 'position']
    list_filter = ['is_sale', 'category', 'type']

    search_fields = ['title', 'price']
    readonly_fields = ['views']
    inlines = [ProductImageInline,ProductDetailsInline]

    prepopulated_fields = {
        'slug': ['title']
    }


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title']
    }


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title']
    }


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title']
    }


@admin.register(SpecialOffer)
class SpecialOfferAdmin(admin.ModelAdmin):
    filter_horizontal = ['products']
    prepopulated_fields = {
        'slug': ['title']
    }
