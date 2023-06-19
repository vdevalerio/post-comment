from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("pc-app/", include("PostCommentApp.urls")),
    path("admin/", admin.site.urls),
]