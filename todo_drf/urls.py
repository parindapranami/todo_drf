
from django.contrib import admin
from django.urls import path, include

#admin djangotodo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('api.urls')),
]
