from django.contrib import admin
from django.urls import path, include

from django.http import JsonResponse

def apiIndex(req):

    return JsonResponse({'msg': 'The api index'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', apiIndex),
    path('api/tracks/', include('api.tracks.urls')),
    path('log-in/', include('users.urls')),
    # path('api/bullets/', include('api.bullets.urls')),
    # path('api/streaks/', include('api.streaks.urls')),
]



