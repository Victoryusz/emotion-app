from django.contrib import admin
from django.urls import path
from emotion.views import emotion_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', emotion_home), # Rota para a página inicial do aplicativo de emoções
]
