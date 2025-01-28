from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User1)



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

admin.site.register(Category, CategoryAdmin)

class PromocodeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

admin.site.register(Promocode, PromocodeAdmin)

class UnitAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

admin.site.register(Unit, UnitAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_new', 'discount')
    search_fields = ('name', 'category__name', 'description')
    list_filter = ('category', 'is_new', 'discount')
    ordering = ('name',)

admin.site.register(Product, ProductAdmin)

