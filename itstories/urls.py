from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from blog.views import StoriesModelViewSet



router = routers.SimpleRouter()
router.register(r'stories', StoriesModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('api/v1/', include(router.urls)),
    path('', include('blog.urls')),


]
