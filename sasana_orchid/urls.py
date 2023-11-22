from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
]