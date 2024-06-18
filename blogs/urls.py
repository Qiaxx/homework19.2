from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import never_cache

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
    path("post/create/", never_cache(BlogCreateView.as_view()), name="post_create"),
    path(
        "post/<int:pk>/update/",
        never_cache(BlogUpdateView.as_view()),
        name="post_update",
    ),
    path(
        "post/<int:pk>/delete/",
        never_cache(BlogDeleteView.as_view()),
        name="post_delete",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
