from django.contrib import admin
from django.urls import path, include

from django.http import JsonResponse

from api.views.index import index
from api.views.report import Report

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('api/', index),
    path('api/report/', Report),
    path('api/tracks/', include('api.tracks.urls')),
    path('users/', include('users.urls')),
    # path('api/bullets/', include('api.bullets.urls')),
    # path('api/streaks/', include('api.streaks.urls')),
]



