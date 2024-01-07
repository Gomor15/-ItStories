from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', StoriesView.as_view(), name='home'),
    path('post/<slug:post_slug>/', StoriesDetailView.as_view(), name='post'),
    path('category/<slug:programming_language_slug>/', StoriesCategory.as_view(), name='category'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('about/', about, name='about'),
    path('contact/', ContactFormView.as_view(), name='contact'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


