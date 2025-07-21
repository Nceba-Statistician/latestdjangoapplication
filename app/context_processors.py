from .models import SidebarCategory

def sidebar_context(request):
    sidebar_categories = SidebarCategory.objects.filter(is_active=True).prefetch_related('items').order_by('order')
    
    # Filter items based on user authentication and staff status
    for category in sidebar_categories:
        category.filtered_items = []
        for item in category.items.filter(is_active=True).order_by('order'):
            if item.requires_login and not request.user.is_authenticated:
                continue
            if item.requires_staff and not (request.user.is_authenticated and request.user.is_staff):
                continue
            category.filtered_items.append(item)

    return {'sidebar_categories': sidebar_categories}