from django.contrib import admin
from .models import Banner,Product

admin.site.register(Banner)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'trending', 'new_arrival')
    prepopulated_fields = {'slug': ('name',)}
