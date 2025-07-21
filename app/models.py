from django.db import models
from django.urls import reverse

class SidebarCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
   
class Meta:
    ordering = ["order", "name"]
    verbose_name_plural = "Sidebar Categories"

def __str__(self):
    return self.name

class SidebarItem(models.Model):
    category = models.ForeignKey(SidebarCategory, on_delete=models.CASCADE, related_name="items")
    title = models.CharField(max_length=100)
    url_name = models.CharField(max_length=100, help_text="url name(e.g., 'app:dashboard')")
    icon_class = models.CharField(max_length=50, blank=True, null=True, help_text="Font Awesome or similar icon class")
    requires_login = models.BooleanField(default=False)
    requires_staff = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
class Meta:
    ordering = ["order", "title"]

def __str__(self):
    return f"{self.title} ({self.category.name})"

def get_absolute_url(self):
    try:
        return reverse(self.url_name)
    except Exception as e:
        return f"error: {e}"

