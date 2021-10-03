from django.contrib import admin
from .models import Product, About, WishList



# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title',]
    list_display_links = ['id', 'title',]


class WishListAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', ]
    list_display_links = ['id', 'title', ]


class AboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'title',]
    list_display_links = ['id', 'title',]


admin.site.register(Product, ProductAdmin)
admin.site.register(WishList, WishListAdmin)
admin.site.register(About, AboutAdmin)
