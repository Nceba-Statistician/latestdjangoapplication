from django.contrib import admin
from .models import SidebarCategory, SidebarItem

class SidebarItemInline(admin.TabularInline):
    model = SidebarItem
    extra = 1
    
@admin.register(SidebarCategory)
class SidebarCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "order", "is_active")
    list_editable = ("order", "is_active")
    inlines = [SidebarItemInline]

@admin.register(SidebarItem)
class SidebarItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url_name', 'icon_class', 'requires_login', 'requires_staff', 'order', 'is_active')
    list_filter = ('category', 'requires_login', 'requires_staff', 'is_active')
    list_editable = ('url_name', 'icon_class', 'requires_login', 'requires_staff', 'order', 'is_active')
    search_fields = ('title', 'url_name')
    