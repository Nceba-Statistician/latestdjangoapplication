from django.urls import path
from . import views

app_name = "Application"

urlpatterns = [
    path("page", views.frontpage, name="page"),
    # path("", views.sidebar, "sidebars"),
    path("", views.product_list_view, name='product_list'),
    path('<int:pk>/', views.product_detail_view, name='product_detail'),
]
