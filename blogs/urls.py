from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from blogs.apps import BlogsConfig
from blogs.views import (
    BlogListView,
    BlogDetailsView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

app_name = BlogsConfig.name

urlpatterns = [
    path("posts/", BlogListView.as_view(), name="post_list"),
    path("post/<int:pk>/", BlogDetailsView.as_view(), name="post_detail"),
    path("post/create/", BlogCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/update/", BlogUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
