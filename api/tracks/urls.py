from django.urls import path, include
from api.tracks.views import *

urlpatterns = [
    path('', Index.as_view()),
    path('<track_id>/', TrackView.as_view()),
    path('<track_id>/entries/', Entries.as_view()),
    path('<track_id>/entries/<entry_id>', Entry.as_view()),
]
