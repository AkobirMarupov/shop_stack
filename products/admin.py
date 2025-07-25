from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from products.models import *


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "brand", "category", "is_active")
    list_display_links = ("id", "name", "brand")
    list_filter = ("is_active", "brand", "category")
    search_fields = ("name", "brand", "category")
    list_editable = ("is_active",)

    fieldsets = (
        (_("Main"), {"fields": ("brand", "category", "is_active")}),
        (
            _("Uzbek"),
            {
                "fields": (
                    "name_uz",
                    "description_uz",
                )
            },
        ),
        (_("English"), {"fields": ("name_en", "description_en")}),
        (_("Russian"), {"fields": ("name_ru", "description_ru")}),
    )


    inlines = [ProductVariantInline]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "logo")
    list_display_links = ("id", "name")
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)



@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "rating", "user__email", "product__name")
    list_display_links = ("id", "rating", "user__email")
    search_fields = ("user__email",)


@admin.register(Commint)
class CommintAdmin(admin.ModelAdmin):
    list_display = ("id", "user__email", "product__name", "commint")
    list_display_links = ("id", "user__email")
    search_fields = ("user__email",)
    