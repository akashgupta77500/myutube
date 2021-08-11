
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.video,name='video'),
    path('videosearch', views.videosearch, name='videosearch'),

  ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)