from django.contrib import admin
from django.urls import path, include
from emotion.views import emotion_home 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pwa.urls')),   # 👈 Coloca o PWA primeiro
    path('', emotion_home),
]
