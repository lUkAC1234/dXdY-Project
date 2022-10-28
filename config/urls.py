from django.contrib import admin
from django.urls import path, include, re_path
from web.views import smth, smth2, smth3, smth4, smth5

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', smth),
    path('', include('web.urls')),
]
