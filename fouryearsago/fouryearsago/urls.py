from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('fya/', include('fya.urls')),
    path('admin/', admin.site.urls),
]
