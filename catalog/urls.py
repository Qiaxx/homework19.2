from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (
    ProductListView,
    ContactsView,
    ProductDetailsView,
    ProductCreateView,
    ProductUpdateView,
)

app_name = CatalogConfig.name


urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("product/<int:pk>/", ProductDetailsView.as_view(), name="product_details"),
    path("product/create/", ProductCreateView.as_view(), name="product_create"),
    path(
        "product/update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
