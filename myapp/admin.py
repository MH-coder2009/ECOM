from django.contrib import admin
from django.utils.html import format_html
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # 1. Columns displayed in the list view
    list_display = ('image_tag', 'name', 'price', 'stock', 'active', 'slug')

    # 2. Right-side filters (only real filters)
    list_filter = ('active',)

    # 3. Search fields
    search_fields = ('name', 'slug', 'description')

    # 4. Read-only fields
    readonly_fields = ('slug',)

    # 5. Default ordering (when page loads)
    ordering = ('price',)

    # 6. Form layout
    fieldsets = (
        ('Main Info', {
            'fields': ('name', 'slug', 'price', 'description')
        }),
        ('Image & Stock', {
            'fields': ('image', 'stock', 'active')
        }),
    )

    # 7. Thumbnail image display
    @admin.display(description='Image')
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 45px; height:45px; border-radius: 5px;" />', obj.image.url)
        return "-"