from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (
    ProductListView,
    ContactsView,
    ProductDetailsView,
    ProductCreateView,
    ProductUpdateView,
    ProductByCategoryView,
    CategoryListView,
)

app_name = CatalogConfig.name


urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path(
        "product/<int:pk>/",
        cache_page(60)(ProductDetailsView.as_view()),
        name="product_details",
    ),
    path("product/create/", ProductCreateView.as_view(), name="product_create"),
    path(
        "product/update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "products/category/<int:category_id>",
        ProductByCategoryView.as_view(),
        name="products_by_category",
    ),
    path("categories/", CategoryListView.as_view(), name="category_list"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
