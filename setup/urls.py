from django.contrib import admin
from django.urls import path, include
from aluraflix_api.views import VideosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('videos', VideosViewSet, basename='Videos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
