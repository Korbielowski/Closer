from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("authentication.urls")),
    path("profile/", include("user_profile.urls")),
    path("search/", include("search.urls")),
    path("invitations/", include("friendship.urls")),
    path("posts", include("posts.urls")),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
