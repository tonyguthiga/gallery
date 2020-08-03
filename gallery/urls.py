from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/', views.search_image, name='search_results'),
    path(r'image/<int:pk>/',views.detail,name = 'detail'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)