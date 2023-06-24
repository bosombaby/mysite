from django.contrib import admin
from .models import Product

# Register your models here.

admin.site.site_header = "二手交易平台"
admin.site.site_title = "manage"
admin.site.index_title = "后台管理"


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'desc')
    list_editable = ('price', 'desc')
    search_fields = ('name', )

    def set_price_to_zero(self,request,queryset):
        queryset.update(price = 0)

    actions = ('set_price_to_zero',)

admin.site.register(Product, ProductAdmin)
